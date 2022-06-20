let i = 2;
$(document).ready(function () {
    // const url = 'http://127.0.0.1:8000/';
    const url = 'http://fortune.radiatnserversite.com/';
    imageDiv = $('#images').show();
    videoDiv = $('#videos').hide();
    $('#image_button').click(function () {
        imageDiv.show();
        videoDiv.hide();
    })
    $('#video_button').click(function () {
        imageDiv.hide();
        videoDiv.show();
    })
    $('.delete_banner').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_footer').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_menu').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_about').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_news').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_media').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_blog').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_testimonial').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    });
    $('.delete_popup').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    });
    $('.delete-form').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    });
    $('.delete_sub_menu').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    });

    $('#popup').modal('show');

    // API call for Menu..................................
    // ......................................
    // var menuIdInSubMenu = [];

    $.when($.ajax("/get_menu"), $.ajax('/get_sub_menu')).done(function (menu, subMenu) {
        var mainMenu = menu[0].data;
        var subMenuList = subMenu[0].data;

        mainMenu.map(a => {
            if (a.menu_position === "topheader") {
                $('.top-header').append(`<li class="nav-item"><a class="nav-link bottom-nav-link text-capitalize" href=${a.menu_link}>` + a.menu_name + '</a></li>')
            } else {
                if (a.menu_type === "dropdown") {
                    var mainMenuId = a.id;
                    console.log("menu id", mainMenuId);
                    var filteredSubMenu = subMenuList.filter((x) => x.menu_id === mainMenuId)
                    $('.bottom-header').append(
                        `<div class="nav-item drop-menu dropdown" id="${a.id}">
                            <button type="button" class="nav-link bottom-nav-link text-capitalize dropdown-toggle input-id" 
                            id="dropdown" data-bs-toggle="dropdown"
                            aria-expanded="false">`
                        + a.menu_name + '</button>' +
                        `<ul class="dropdown-menu" aria-labelledby="dropdown" id="submenu-${a.id}">` +
                        '</ul></div>'
                    )
                    filteredSubMenu.map(b => {
                        $(`#submenu-${mainMenuId}`).append(`<li><a class="dropdown-item text-capitalize" href="${url}sub_menu/${b.id}">` + b.sub_menu_name + '</a></li>')
                    })
                } else {
                    if (a.menu_link === '' || a.menu_link === null) {
                        $('.bottom-header').append(
                            `<a class="nav-link text-capitalize bottom-nav-link text-dark" href="${url}fortune/${a.id}">`
                            + a.menu_name +
                            '</a>'
                        )
                    } else {
                        $('.bottom-header').append(
                            `<a class="nav-link text-capitalize bottom-nav-link text-dark" href="${url}${a.menu_link}">`
                            + a.menu_name +
                            '</a>'
                        )
                    }

                }
            }
        })
        console.log("new menu", mainMenu);
        console.log("new sub menu", subMenuList);
    });

    // main menu based on selected value....................
    var linkContent = $('.link-content').hide();
    $('#menu-type').change(function () {
        var val = $(this).val();
        if (val === 'link') {
            linkContent.show();
        } else {
            linkContent.hide();
        }
    })



    // news based on selected value
    var newsIdentity = $('.news-identity').hide();
    var news = $('.news').show();
    $('#news_position').change(function () {
        var val = $(this).val();
        if (val === 'news_identity') {
            newsIdentity.show();
            news.hide();
        } else {
            newsIdentity.hide();
            news.show();
        }
    })


    // circular loop.................

    var radius = 250;
    var fields = $('.circleItem');
    var container = $('.circleContent');
    var width = container.width();
    radius = width / 2.4;

    var height = container.height();
    var angle = 0, step = (2 * Math.PI) / fields.length;
    fields.each(function () {
        var x = Math.round(width / 2 + radius * Math.cos(angle) - $(this).width() / 2);
        var y = Math.round(height / 2 + radius * Math.sin(angle) - $(this).height() / 2);
        if (window.console) {
            console.log($(this).text(), x, y);
        }

        $(this).css({
            left: x + 'px',
            top: y + 'px'
        });
        angle += step;
    });

    // counter part...............
    function count($this) {
        var current = parseInt($this.html(), 10);
        current = current + 1; /* Where 1 is increment */

        $this.html(++current);
        if (current > $this.data('count')) {
            $this.html($this.data('count'));
        } else {
            setTimeout(function () { count($this) }, 10);
        }
    }

    jQuery(".counter").each(function () {
        jQuery(this).data('count', parseInt(jQuery(this).html(), 10));
        jQuery(this).html('0');
        count(jQuery(this));
    });

    // Fixed header on scroll
    $(window).scroll(function () {
        var sticky = $('.sticky'),
            scroll = $(window).scrollTop();

        if (scroll >= 100) sticky.addClass('fixed');
        else sticky.removeClass('fixed');
    });
});
