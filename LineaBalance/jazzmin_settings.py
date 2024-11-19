# CONFIGURACIONES DE JAZZMIN PARA CUSTOMIZAR EL PANEL ADMIN DE DJANGO
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "LOBMS",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "LOBMS",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "LOBMS",

    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "grafico-de-linea.png",LOGOLOBMS.jpg
    "site_logo": "LOGOLOBMS.jpg",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    # "login_logo": "grafico-de-linea.png",LOGOLOBMS
    "login_logo": "LOGOLOBMS.jpg",

    # Logo to use for login form in dark themes (defaults to login_logo)
    # "login_logo_dark": "grafico-de-linea.png",
    "login_logo_dark": "LOGOLOBMS.jpg",

    # CSS classes that are applied to the logo above
    # "site_logo_classes": "img-circle",
    "site_logo_classes": "rounded",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Administra tus lineas de balance",

    # Copyright on the footer
    "copyright": " Constructora del Mar II",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Soporte", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
    ],
    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Soporte", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True, "icon":"fa-solid fa-circle-info"},
        {"name": "Api-Docs", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True, "icon":"fa-solid fa-book"},
        {"model": "auth.user"}
    ],
    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["Seguimiento.Periodo", "Seguimiento.Proyecto",
                              "Seguimiento.Fase", "Seguimiento.Partida",
                              "Seguimiento.Balance", "Seguimiento.DetalleBalance"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "seguimiento": [{
            "name": "Enlace 1",
            # "url": "#",
            "icon": "fa-solid fa-up-right-from-square",
            # "permissions": ["books.view_book"]
        }, {
            "name": "Enlace 2",
            # "url": "hola#",
            "icon": "fa-solid fa-up-right-from-square",
            # "permissions": ["books.view_book"]
        }]
    },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "Seguimiento.Partida": "fa-solid fa-trowel-bricks",
        "Seguimiento.DetalleBalance": "fa-solid fa-chart-line",
        "Seguimiento.Proyecto": "fa-duotone fa-solid fa-building-wheat",
        "Seguimiento.Periodo": "fa-regular fa-calendar-days",
        "Seguimiento.Balance": "fa-solid fa-check-to-slot",
        "Seguimiento.Fase": "fa-solid fa-landmark",

    },

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    # "related_modal_active": True,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "collapsible",
    # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs", "Seguimiento.Balance": "horizontal_tabs"},
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    # "language_chooser": True,

}
JAZZMIN_UI_TWEAKS = {
    # "theme": "slate",
    # "theme": "solar",
    # "theme": "superhero",
    # "theme": "cosmo",
    # "theme": "journal",
    # "theme": "materia",
    # "theme": "litera",
    # "theme": "minty",
    # "theme": "sandstone",
    # "theme": "united",

    # "dark_mode_theme": "darkly",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}