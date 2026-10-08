document.addEventListener('DOMContentLoaded', () => {
    // 1. Sticky Navbar & Active Link Update
    const navbar = document.getElementById('navbar');
    const sections = document.querySelectorAll('section, header');
    const navLinks = document.querySelectorAll('.nav-link');
    const backToTopBtn = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        // Sticky Navbar
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Back to Top Button
        if (window.scrollY > 500) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }

        // Active Link Update
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active');
            }
        });
    });

    // 2. Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu');
    const navMenu = document.getElementById('nav-menu');

    mobileMenuBtn.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when a link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
        });
    });

    // 3. Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            // If it's just a dummy link (e.g. href="#"), prevent default and do nothing
            if(targetId === '#') {
                e.preventDefault();
                return;
            }
            
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                e.preventDefault();
                const navHeight = navbar.offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - navHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Back to top click
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // 4. Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const elementVisible = 100;

        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            if (elementTop < windowHeight - elementVisible) {
                element.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger on load

    // 5. Gallery Filter
    const filterBtns = document.querySelectorAll('.filter-btn');
    const masonryItems = document.querySelectorAll('.masonry-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            masonryItems.forEach(item => {
                if (filterValue === 'all' || item.classList.contains(filterValue)) {
                    item.classList.remove('hide');
                } else {
                    item.classList.add('hide');
                }
            });
        });
    });

    // UMKM Filter
    const umkmFilterBtns = document.querySelectorAll('.umkm-filter-btn');
    const umkmItems = document.querySelectorAll('.umkm-item');

    umkmFilterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            umkmFilterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            umkmItems.forEach(item => {
                if (filterValue === 'all' || item.classList.contains(filterValue)) {
                    item.classList.remove('hide');
                } else {
                    item.classList.add('hide');
                }
            });
        });
    });

    // 6. Lightbox for Gallery
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const closeLightbox = document.querySelector('.close-lightbox');

    // Make all masonry images clickable
    document.querySelectorAll('.masonry-item img').forEach(img => {
        img.addEventListener('click', function() {
            lightbox.style.display = "block";
            lightboxImg.src = this.src;
            const caption = this.nextElementSibling ? this.nextElementSibling.innerText : '';
            lightboxCaption.innerHTML = caption;
            
            // Prevent body scroll
            document.body.style.overflow = 'hidden';
        });
    });

    // Close lightbox
    const closeBox = () => {
        lightbox.style.display = "none";
        document.body.style.overflow = 'auto';
    }
    
    closeLightbox.addEventListener('click', closeBox);
    
    lightbox.addEventListener('click', (e) => {
        if(e.target === lightbox) {
            closeBox();
        }
    });
    
    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && lightbox.style.display === 'block') {
            closeBox();
        }
    });

    // 7. Tabs Switching (General Function)
    function setupTabs(btnClass, panelClass, defaultColor, activeColor) {
        const btns = document.querySelectorAll(btnClass);
        const panels = document.querySelectorAll(panelClass);

        btns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Reset all
                btns.forEach(b => {
                    b.classList.remove('active');
                    if(defaultColor) b.style.color = defaultColor;
                });
                panels.forEach(p => {
                    p.style.display = 'none';
                    p.classList.add('hidden'); // if using hidden class
                });

                // Activate clicked
                btn.classList.add('active');
                if(activeColor) btn.style.color = activeColor;
                
                const targetId = btn.getAttribute('data-tab');
                const targetPanel = document.getElementById(targetId);
                if(targetPanel) {
                    targetPanel.style.display = 'block';
                    targetPanel.classList.remove('hidden');
                }
            });
        });
    }

    // Initialize all tabs
    setupTabs('.rt-tab-btn', '.rt-panel', null, null); // RT Tabs
    setupTabs('.kt-tab-btn', '.kt-panel', '#666', 'var(--color-primary-dark)'); // Karang Taruna Tabs
    setupTabs('.dnm-tab-btn', '.dnm-panel', '#666', 'var(--color-primary-dark)'); // Dinamika Tabs

});
