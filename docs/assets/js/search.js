(function () {
    'use strict';

    var results = document.getElementById('lunrsearchresults');
    var query = (new URLSearchParams(window.location.search).get('q') || '').trim();
    var input = document.getElementById('lunrsearch');
    if (input) input.value = query;

    function normalize(text) {
        return text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    }

    function message(title, body) {
        var box = document.createElement('div');
        box.className = 'br-message info';
        var content = document.createElement('div');
        content.className = 'content';
        var heading = document.createElement('strong');
        heading.textContent = title + ' ';
        content.append(heading, document.createTextNode(body));
        box.appendChild(content);
        results.appendChild(box);
    }

    if (!query) {
        message('Sem termo de busca.', 'Por favor, informe o texto que deseja pesquisar.');
        return;
    }

    // Treat the query as text, including punctuation, and ignore case and accents.
    var terms = Array.from(new Set(normalize(query).split(/\s+/).filter(Boolean))).sort(function (a, b) {
        return b.length - a.length;
    });
    if (!terms.length) {
        message('Sem termo de busca.', 'Por favor, informe o texto que deseja pesquisar.');
        return;
    }
    var pattern = new RegExp(terms.map(function (term) {
        return term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }).join('|'), 'g');

    function matches(text) {
        return terms.some(function (term) { return normalize(text).includes(term); });
    }

    function highlight(container) {
        var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT);
        var nodes = [];
        var text = '';
        while (walker.nextNode()) {
            nodes.push({ node: walker.currentNode, start: text.length });
            text += walker.currentNode.nodeValue;
        }
        // Keep offsets into the original text, including decomposed accents.
        var folded = '';
        var offsets = [];
        var offset = 0;
        for (var character of text) {
            var normalized = normalize(character);
            for (var i = 0; i < normalized.length; i++) offsets.push(offset);
            folded += normalized;
            offset += character.length;
        }
        offsets.push(text.length);
        pattern.lastIndex = 0;
        var ranges = [];
        var match;
        while ((match = pattern.exec(folded)) !== null) {
            ranges.push([offsets[match.index], offsets[match.index + match[0].length]]);
        }
        nodes.forEach(function (entry) {
            var value = entry.node.nodeValue;
            var fragment = document.createDocumentFragment();
            var cursor = 0;
            ranges.forEach(function (range) {
                var start = Math.max(0, range[0] - entry.start);
                var end = Math.min(value.length, range[1] - entry.start);
                if (start >= end) return;
                fragment.appendChild(document.createTextNode(value.slice(cursor, start)));
                var mark = document.createElement('mark');
                mark.textContent = value.slice(start, end);
                fragment.appendChild(mark);
                cursor = end;
            });
            fragment.appendChild(document.createTextNode(value.slice(cursor)));
            entry.node.replaceWith(fragment);
        });
    }

    function prepare(doc) {
        var root = document.createElement('div');
        root.innerHTML = doc.html;
        root.querySelectorAll('script, style, iframe, object, embed, form, template, nav, [hidden], [aria-hidden="true"]').forEach(function (node) {
            node.remove();
        });
        root.querySelectorAll('*').forEach(function (node) {
            Array.from(node.attributes).forEach(function (attribute) {
                if (/^on/i.test(attribute.name) || attribute.name === 'srcdoc') node.removeAttribute(attribute.name);
            });
            ['href', 'src'].forEach(function (attribute) {
                var value = node.getAttribute(attribute);
                if (!value) return;
                try {
                    var url = new URL(value, new URL(doc.url, window.location.origin));
                    if (!['http:', 'https:', 'mailto:', 'tel:'].includes(url.protocol)) {
                        node.removeAttribute(attribute);
                    } else {
                        node.setAttribute(attribute, url.href);
                    }
                } catch (_) {
                    node.removeAttribute(attribute);
                }
            });
            if (node.tagName === 'IMG') node.loading = 'lazy';
        });
        return root;
    }

    function sections(root) {
        var headings = Array.from(root.querySelectorAll('h1, h2, h3, h4, h5, h6'));
        var pieces = [];
        // An introductory passage is searchable even before the first heading.
        [null].concat(headings).forEach(function (heading, index) {
            var range = document.createRange();
            if (heading) range.setStartBefore(heading);
            else range.setStart(root, 0);
            if (headings[index]) range.setEndBefore(headings[index]);
            else range.setEnd(root, root.childNodes.length);
            var content = document.createElement('div');
            content.className = 'search-section-content';
            content.appendChild(range.cloneContents());
            if (matches(content.textContent)) pieces.push({
                content: content,
                anchor: heading && heading.id,
                title: heading ? heading.textContent : 'Introdução'
            });
        });
        return pieces;
    }

    function excerpt(content) {
        content.querySelectorAll('h1, h2, h3, h4, h5, h6, img').forEach(function (node) { node.remove(); });
        highlight(content);
        var first = content.querySelector('mark');
        if (!first) return null;
        var block = first.closest('p, li, td, th, blockquote, pre') || content;
        var walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT);
        var nodes = [];
        var text = '';
        var position = 0;
        while (walker.nextNode()) {
            if (first.contains(walker.currentNode)) position = text.length;
            nodes.push({ node: walker.currentNode, start: text.length });
            text += walker.currentNode.nodeValue;
        }
        // Keep a short, real fragment of the formatted text around the first occurrence.
        var start = Math.max(0, position - 70);
        var end = Math.min(text.length, Math.max(start + 240, position + first.textContent.length));
        while (start > 0 && start < position && !/\s/.test(text[start - 1])) start++;
        while (end < text.length && end > position + first.textContent.length && !/\s/.test(text[end])) end--;
        var range = document.createRange();
        var firstNode = nodes.find(function (entry) { return entry.start + entry.node.length > start; });
        var lastNode = nodes.find(function (entry) { return entry.start + entry.node.length >= end; });
        range.setStart(firstNode.node, start - firstNode.start);
        range.setEnd(lastNode.node, end - lastNode.start);
        var fragment = document.createElement('div');
        fragment.className = 'search-section-content';
        if (start) fragment.appendChild(document.createTextNode('… '));
        fragment.appendChild(range.cloneContents());
        if (end < text.length) fragment.appendChild(document.createTextNode(' …'));
        fragment.querySelectorAll('[id]').forEach(function (node) { node.removeAttribute('id'); });
        fragment.querySelectorAll('mark').forEach(function (node) { node.replaceWith(document.createTextNode(node.textContent)); });
        highlight(fragment);
        return fragment;
    }

    var menuData = document.getElementById('search-menu');
    var menuPaths = new Map();
    function pagePath(url) {
        return new URL(url, window.location.origin).pathname
            .replace(/\/index\.html$/, '/').replace(/\.html$/, '').replace(/\/$/, '');
    }
    function indexMenu(items, parents) {
        items.forEach(function (item) {
            var path = parents.concat(item.title);
            if (item.href && item.href.startsWith('/') && !item.href.startsWith('//')) {
                var key = pagePath((menuData.dataset.baseurl || '') + item.href);
                if (!menuPaths.has(key)) menuPaths.set(key, parents);
            }
            if (item.children) indexMenu(item.children, path);
        });
    }
    if (menuData) indexMenu(JSON.parse(menuData.textContent), []);

    var documents = JSON.parse(document.getElementById('search-documents').textContent);
    var count = 0;
    var summary = document.createElement('p');
    results.appendChild(summary);
    documents.forEach(function (doc) {
        var root = prepare(doc);
        var searchable = normalize(doc.title + ' ' + root.textContent);
        if (!terms.every(function (term) { return searchable.includes(term); })) return;
        var found = sections(root);
        if (!found.length && !matches(doc.title)) return;
        count++;
        var article = document.createElement('details');
        article.className = 'search-result';
        article.setAttribute('name', 'search-pages');
        var toggle = document.createElement('summary');
        toggle.className = 'search-result-summary';
        var heading = document.createElement('span');
        heading.className = 'search-result-title';
        var parents = menuPaths.get(pagePath(doc.url)) || [];
        heading.textContent = parents.concat(doc.title).join(' › ');
        highlight(heading);
        var meta = document.createElement('span');
        meta.className = 'search-result-count';
        meta.textContent = found.length ? found.length + (found.length === 1 ? ' seção' : ' seções') : 'No título';
        toggle.append(heading, meta);
        article.appendChild(toggle);
        article.addEventListener('toggle', function () {
            if (article.open) results.querySelectorAll('.search-result[open]').forEach(function (other) {
                if (other !== article) other.open = false;
            });
        });
        var body = document.createElement('div');
        body.className = 'search-result-body';
        var link = document.createElement('a');
        link.href = doc.url;
        link.className = 'search-page-link';
        link.textContent = 'Abrir página completa';
        body.appendChild(link);
        var additional = document.createElement('details');
        additional.className = 'search-more-sections';
        var more = document.createElement('summary');
        more.textContent = 'Ver mais ' + (found.length - 3) + ' seções';
        additional.appendChild(more);
        found.forEach(function (section, index) {
            var wrapper = document.createElement('section');
            wrapper.className = 'search-section';
            var sectionHeading = document.createElement('h3');
            var original = document.createElement('a');
            original.className = 'search-section-link';
            original.href = doc.url + (section.anchor ? '#' + encodeURIComponent(section.anchor) : '');
            original.textContent = section.title;
            highlight(original);
            sectionHeading.appendChild(original);
            wrapper.appendChild(sectionHeading);
            var fragment = excerpt(section.content);
            if (fragment) wrapper.appendChild(fragment);
            (index < 3 ? body : additional).appendChild(wrapper);
        });
        if (found.length > 3) body.appendChild(additional);
        article.appendChild(body);
        results.appendChild(article);
    });
    if (count) {
        summary.textContent = count + (count === 1 ? ' página encontrada' : ' páginas encontradas') + ' para “' + query + '”.';
    } else {
        summary.remove();
        message('Sem resultados.', 'Não encontramos páginas correspondentes. Tente outro termo.');
    }
}());
