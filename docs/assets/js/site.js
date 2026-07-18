document.addEventListener("DOMContentLoaded", function () {

  const menuButton = document.getElementById("navigation");
  const menuContainer = document.getElementById("menuref");
  const menuCloseButton = document.getElementById("close-menu");
  const menu = document.getElementById("main-navigation");

  // Armazena as classes originais APENAS se o menu não estiver oculto por padrão (no desktop)
  let originalClasses = menuContainer.className;

  // --- Lógica para ocultar no celular por padrão ---
  const isMobile = () => window.innerWidth < 992; // 992px é um valor indicado para breakpoint de mobile/tablet

  if (isMobile() && !menuContainer.classList.contains("d-none")) {
    // Se "mobile" o menu por padrão não irá aparecer
    menuContainer.className = "";
    menuContainer.classList.add("d-none");
  }
  // --- Fim da Lógica de ocultar no celular por padrão ---

  menuButton.addEventListener("click", function () {
    // Se o elemento raiz do menu tiver a classe 'd-none' (oculto)
    if (menuContainer.classList.contains("d-none")) {
      // Restaura as classes originais (mostra o menu)
      menuContainer.className = originalClasses;
      menu.classList.add("active");
    } else {
      // Oculta a div superior e remove menu ativo
      menuContainer.className = "";
      menu.classList.remove("active");
      menuContainer.classList.add("d-none");
    }
  });

  menuCloseButton.addEventListener("click", function () {
    // Oculta a div superior do menu
    menuContainer.className = "";
    menu.classList.remove("active");
    menuContainer.classList.add("d-none");
  })

  // lógica para implementar cópia da URL
  const copyUrlButton = document.getElementById("copyUrlButton");
  // cria listener para o botao de copiar e escreve url atual para área de transferência
  if (copyUrlButton) { // Boa prática: verifica se o botão existe antes de adicionar o listener
    copyUrlButton.addEventListener("click", function () {
      // Verifica se a API está disponível (não deve falhar na maioria dos navegadores modernos)
      if (navigator.clipboard) {
        navigator.clipboard.writeText(window.location.href)
          .then(() => {
            // Opcional: Feedback visual de que copiou
            console.log("URL copiada!");
          })
          .catch(err => {
            console.error('Falha ao copiar: ', err);
          });
      } else {
        // Fallback para navegadores sem a API
        console.warn('A API navigator.clipboard não está disponível.');
        // Pode-se usar um método antigo aqui, como `document.execCommand('copy')`
      }
    });
  }

  // Fallback para ambientes onde o plugin jekyll-toc nao e executado (ex.: build padrao do GitHub Pages)
  const mainContent = document.getElementById("main-content");
  const tocEnabled = mainContent && mainContent.dataset.tocEnabled === "true";
  const hasRenderedToc = mainContent && mainContent.querySelector(".section-nav, #markdown-toc");
  if (tocEnabled && !hasRenderedToc) {
    const headings = Array.from(mainContent.querySelectorAll("h1, h2, h3, h4, h5, h6"));

    if (headings.length > 0) {
      const toc = document.createElement("ul");
      toc.className = "section-nav";

      headings.forEach((heading, index) => {
        if (!heading.id) {
          const baseId = heading.textContent
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .replace(/[^a-z0-9\s-]/g, "")
            .trim()
            .replace(/\s+/g, "-") || `secao-${index + 1}`;

          let uniqueId = baseId;
          let suffix = 2;
          while (document.getElementById(uniqueId)) {
            uniqueId = `${baseId}-${suffix}`;
            suffix += 1;
          }
          heading.id = uniqueId;
        }

        const level = heading.tagName.toLowerCase();
        const li = document.createElement("li");
        li.className = `toc-entry toc-${level}`;

        const a = document.createElement("a");
        a.href = `#${heading.id}`;
        a.textContent = heading.textContent.trim();

        li.appendChild(a);
        toc.appendChild(li);
      });

      mainContent.insertBefore(toc, mainContent.firstChild);
    }
  }
});