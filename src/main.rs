pub mod play_button;

use gtk::gdk::Display;
use gtk::prelude::*;
use gtk::{
    gio, glib, Application, ApplicationWindow, CssProvider, StyleContext,
    STYLE_PROVIDER_PRIORITY_APPLICATION,
};
use play_button::PlayButton;

macro_rules! add_icons_resource_path {
    ($icons:expr) => {
        let theme = gtk::IconTheme::for_display(&Display::default().unwrap());
        theme.add_resource_path($icons);
    };
}

fn build_file_menu() -> gio::Menu {
    let menu = gio::Menu::new();
    /* -------------------------------------------------------------------------- */
    /*                                New Playlist                                */
    /* -------------------------------------------------------------------------- */
    menu.append(Some("New Playlist"), Some("app.new.playlist"));

    /* -------------------------------------------------------------------------- */
    /*                                    Open                                    */
    /* -------------------------------------------------------------------------- */
    menu.append(Some("Open..."), Some("app.open"));

    /* -------------------------------------------------------------------------- */
    /*                                 Separator 1                                */
    /* -------------------------------------------------------------------------- */
    let io = gio::Menu::new();

    /* -------------------------------------------------------------------------- */
    /*                                 Import Menu                                */
    /* -------------------------------------------------------------------------- */
    let import = gio::Menu::new();

    /* ------------------------------- Import File ------------------------------ */
    import.append(Some("File..."), Some("app.import.file"));

    /* ------------------------------ Import Folder ----------------------------- */
    import.append(Some("Folder..."), Some("app.import.folder"));

    /* ----------------------------- Import Playlist ---------------------------- */
    import.append(Some("Playlist..."), Some("app.import.playlist"));
    io.append_submenu(Some("Import"), &import);

    /* -------------------------------------------------------------------------- */
    /*                                   Export                                   */
    /* -------------------------------------------------------------------------- */
    io.append(Some("Export Playlist..."), Some("app.export"));
    menu.append_section(None, &io);

    /* -------------------------------------------------------------------------- */
    /*                                 Separator 2                                */
    /* -------------------------------------------------------------------------- */
    let quit = gio::Menu::new();

    /* -------------------------------------------------------------------------- */
    /*                                    Quit                                    */
    /* -------------------------------------------------------------------------- */
    quit.append(Some("Quit"), Some("app.quit"));
    menu.append_section(None, &quit);

    menu
}

fn build_edit_menu() -> gio::Menu {
    let menu = gio::Menu::new();
    menu.append(Some("Undo"), Some("app.undo"));
    menu.append(Some("Redo"), Some("app.redo"));
    let clipboard = gio::Menu::new();
    clipboard.append(Some("Cut"), Some("app.cut"));
    clipboard.append(Some("Copy"), Some("app.copy"));
    clipboard.append(Some("Paste"), Some("app.paste"));
    menu.append_section(None, &clipboard);
    let find_replace = gio::Menu::new();
    find_replace.append(Some("Find"), Some("app.find"));
    find_replace.append(Some("Replace"), Some("app.replace"));
    menu.append_section(None, &find_replace);
    let separator = gio::Menu::new();
    separator.append(Some("Preferences"), Some("app.preferences"));
    menu.append_section(None, &separator);
    menu
}

fn build_help_menu() -> gio::Menu {
    let menu = gio::Menu::new();
    menu.append(Some("Help"), Some("app.help"));
    menu.append(Some("About"), Some("app.about"));
    menu
}

fn build_menu(app: &gtk::Application) {
    let menu = gio::Menu::new();
    let file_menu = build_file_menu();
    menu.append_submenu(Some("File"), &file_menu);
    let edit_menu = build_edit_menu();
    menu.append_submenu(Some("Edit"), &edit_menu);
    let help_menu = build_help_menu();
    menu.append_submenu(Some("Help"), &help_menu);
    app.set_menubar(Some(&menu));
}

fn add_accelerators(app: &gtk::Application) {
    /* -------------------------------- File Menu ------------------------------- */
    app.set_accels_for_action("app.new.playlist", &["<Primary>N"]);
    app.set_accels_for_action("app.open", &["<Primary>O"]);
    app.set_accels_for_action("app.quit", &["<Primary>Q"]);

    /* -------------------------------- Edit Menu ------------------------------- */
    app.set_accels_for_action("app.undo", &["<Primary>Z"]);
    app.set_accels_for_action("app.redo", &["<Primary><Shift>Z"]);
    app.set_accels_for_action("app.cut", &["<Primary>X"]);
    app.set_accels_for_action("app.copy", &["<Primary>C"]);
    app.set_accels_for_action("app.paste", &["<Primary>V"]);
    app.set_accels_for_action("app.find", &["<Primary>F"]);
    app.set_accels_for_action("app.replace", &["<Primary>H"]);

    /* -------------------------------- Help Menu ------------------------------- */
    app.set_accels_for_action("app.help", &["F1"]);
}

fn add_actions(app: &gtk::Application, window: &gtk::ApplicationWindow) {
    let new_playlist = gio::SimpleAction::new("new.playlist", None);
    new_playlist.connect_activate(|_, _| {
        println!("New Playlist");
    });
    app.add_action(&new_playlist);

    let open = gio::SimpleAction::new("open", None);
    open.connect_activate(|_, _| {
        println!("Open");
    });
    app.add_action(&open);

    let import_file = gio::SimpleAction::new("import.file", None);
    import_file.connect_activate(|_, _| {
        println!("Import File");
    });
    app.add_action(&import_file);

    let import_folder = gio::SimpleAction::new("import.folder", None);
    import_folder.connect_activate(|_, _| {
        println!("Import Folder");
    });
    app.add_action(&import_folder);

    let import_playlist = gio::SimpleAction::new("import.playlist", None);
    import_playlist.connect_activate(|_, _| {
        println!("Import Playlist");
    });
    app.add_action(&import_playlist);

    let export = gio::SimpleAction::new("export", None);
    export.connect_activate(|_, _| {
        println!("Export Playlist");
    });
    app.add_action(&export);

    let quit = gio::SimpleAction::new("quit", None);
    quit.connect_activate(glib::clone!(@weak window => move |_, _| {
        window.close();
    }));
    app.add_action(&quit);

    /* -------------------------------- Edit Menu ------------------------------- */
    let undo = gio::SimpleAction::new("undo", None);
    undo.connect_activate(|_, _| {
        println!("Undo");
    });
    app.add_action(&undo);

    let redo = gio::SimpleAction::new("redo", None);
    redo.connect_activate(|_, _| {
        println!("Redo");
    });
    app.add_action(&redo);

    let cut = gio::SimpleAction::new("cut", None);
    cut.connect_activate(|_, _| {
        println!("Cut");
    });
    app.add_action(&cut);

    let copy = gio::SimpleAction::new("copy", None);
    copy.connect_activate(|_, _| {
        println!("Copy");
    });
    app.add_action(&copy);

    let paste = gio::SimpleAction::new("paste", None);
    paste.connect_activate(|_, _| {
        println!("Paste");
    });
    app.add_action(&paste);

    let find = gio::SimpleAction::new("find", None);
    find.connect_activate(|_, _| {
        println!("Find");
    });
    app.add_action(&find);

    let replace = gio::SimpleAction::new("replace", None);
    replace.connect_activate(|_, _| {
        println!("Replace");
    });
    app.add_action(&replace);

    let preferences = gio::SimpleAction::new("preferences", None);
    preferences.connect_activate(|_, _| {
        println!("Preferences");
    });
    app.add_action(&preferences);

    /* -------------------------------- Help Menu ------------------------------- */
    let help = gio::SimpleAction::new("help", None);
    help.connect_activate(|_, _| {
        println!("Help");
    });
    app.add_action(&help);

    let about = gio::SimpleAction::new("about", None);
    about.connect_activate(|_, _| {
        println!("About");
    });
    app.add_action(&about);
}

fn build_ui(app: &gtk::Application) {
    let window: ApplicationWindow = ApplicationWindow::builder()
        .application(app)
        .title("MP3 Player")
        .default_width(800)
        .default_height(600)
        .build();
    window.set_show_menubar(true);

    let vbox = gtk::Box::new(gtk::Orientation::Vertical, 0);
    let play_button = PlayButton::new();
    vbox.append(&play_button);
    window.set_child(Some(&vbox));

    build_menu(app);

    add_actions(app, &window);

    app.connect_activate(move |_| {
        window.show();
    });
}

fn main() {
    dotenv::dotenv().ok();
    let bytes = glib::Bytes::from_static(include_bytes!("resources.gresource"));
    let resource = gio::Resource::from_data(&bytes).unwrap();
    gio::resources_register(&resource);
    let application = Application::builder()
        .application_id("org.ncc.mp3player")
        .build();

    application.connect_startup(|app| {
        let provider = CssProvider::new();
        provider.load_from_data(include_bytes!("data/style.css"));

        // We give the CssProvided to the default screen so the CSS rules we added
        // can be applied to our window.
        StyleContext::add_provider_for_display(
            &Display::default().expect("Could not connect to a display."),
            &provider,
            STYLE_PROVIDER_PRIORITY_APPLICATION,
        );
        add_icons_resource_path!("/org/ncc/mp3player/data/icons/symbolic");
        add_accelerators(app);
        build_ui(app);
    });

    application.run();
}
