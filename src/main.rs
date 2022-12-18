use gtk::prelude::*;
use gtk::{Application, ApplicationWindow, HeaderBar};

/// Build the File menu
/// # Arguments
/// * `app` - The application
/// # Returns
/// The File menu
/// # Example
/// ```
/// let file_menu = build_file_menu(app);
/// ```
/// # Safety
/// This function is unsafe because it calls the `connect_activate` method on the menu items which is unsafe.
/// # Panic
/// This function will panic if the `connect_activate` method panics.
fn build_file_menu(app: Application) -> gtk::Menu {
    let menu = gtk::Menu::new();

    /* -------------------------------------------------------------------------- */
    /*                                New Playlist                                */
    /* -------------------------------------------------------------------------- */
    let new_playlist = gtk::MenuItem::builder()
        .label("New Playlist")
        .accel_path("<MP3Player>/File/New Playlist")
        .build();
    new_playlist.connect_activate(|_| {
        println!("New Playlist");
    });
    menu.append(&new_playlist);

    /* -------------------------------------------------------------------------- */
    /*                                    Open                                    */
    /* -------------------------------------------------------------------------- */
    let open = gtk::MenuItem::builder()
        .label("Open")
        .accel_path("<MP3Player>/File/Open")
        .build();
    open.connect_activate(|_| {
        println!("Open");
    });
    menu.append(&open);

    /* -------------------------------------------------------------------------- */
    /*                                 Separator 1                                */
    /* -------------------------------------------------------------------------- */
    let separator = gtk::SeparatorMenuItem::new();
    menu.append(&separator);

    /* -------------------------------------------------------------------------- */
    /*                                   Import                                   */
    /* -------------------------------------------------------------------------- */
    let import = gtk::Menu::new();

    /* ------------------------------- Import File ------------------------------ */
    let import_file = gtk::MenuItem::builder()
        .label("File")
        .accel_path("<MP3Player>/File/Import/File")
        .build();
    import_file.connect_activate(|_| {
        println!("Import File");
    });
    import.append(&import_file);

    /* ------------------------------- Import Folder ------------------------------ */
    let import_folder = gtk::MenuItem::builder()
        .label("Folder")
        .accel_path("<MP3Player>/File/Import/Folder")
        .build();
    import_folder.connect_activate(|_| {
        println!("Import Folder");
    });
    import.append(&import_folder);

    /* ------------------------------- Import Playlist ------------------------------ */
    let import_playlist = gtk::MenuItem::builder()
        .label("Playlist")
        .accel_path("<MP3Player>/File/Import/Playlist")
        .build();
    import_playlist.connect_activate(|_| {
        println!("Import Playlist");
    });
    import.append(&import_playlist);

    /* ------------------------------- Import Item ------------------------------ */
    let import_item = gtk::MenuItem::builder()
        .label("Import")
        .accel_path("<MP3Player>/File/Import")
        .submenu(&import)
        .build();
    menu.append(&import_item);

    /* -------------------------------------------------------------------------- */
    /*                                   Export                                   */
    /* -------------------------------------------------------------------------- */
    let export = gtk::MenuItem::builder()
        .label("Export Playlist")
        .accel_path("<MP3Player>/File/Export Playlist")
        .build();
    export.connect_activate(|_| {
        println!("Export Playlist");
    });
    menu.append(&export);

    /* -------------------------------------------------------------------------- */
    /*                                 Separator 2                                */
    /* -------------------------------------------------------------------------- */
    let separator = gtk::SeparatorMenuItem::new();
    menu.append(&separator);

    /* -------------------------------------------------------------------------- */
    /*                                    Quit                                    */
    /* -------------------------------------------------------------------------- */
    let quit = gtk::MenuItem::builder()
        .label("Quit")
        .accel_path("<MP3Player>/File/Quit")
        .build();
    quit.connect_activate(move |_| {
        app.quit();
    });
    menu.append(&quit);
    /* -------------------------------------------------------------------------- */
    menu
}

/// Build the Edit menu
fn build_edit_menu() -> gtk::Menu {
    let menu = gtk::Menu::new();

    /* -------------------------------------------------------------------------- */
    /*                                  Preference                                */
    /* -------------------------------------------------------------------------- */
    let preferences = gtk::MenuItem::builder()
        .label("Preferences")
        .accel_path("<MP3Player>/Edit/Preferences")
        .build();
    preferences.connect_activate(|_| {
        println!("Preferences");
    });
    menu.append(&preferences);
    /* -------------------------------------------------------------------------- */
    menu
}

fn build_help_menu() -> gtk::Menu {
    let menu = gtk::Menu::new();
    /* -------------------------------------------------------------------------- */
    /*                                    About                                   */
    /* -------------------------------------------------------------------------- */
    let about = gtk::MenuItem::builder()
        .label("About")
        .accel_path("<MP3Player>/Help/About")
        .build();
    about.connect_activate(|_| {
        println!("About");
    });
    menu.append(&about);
    /* -------------------------------------------------------------------------- */
    menu
}

fn build_menu(app: Application) -> gtk::MenuBar {
    let menu_bar = gtk::MenuBar::new();

    /* -------------------------------------------------------------------------- */
    /*                                  File Menu                                 */
    /* -------------------------------------------------------------------------- */
    let file_menu = build_file_menu(app);
    let file_menu_item = gtk::MenuItem::builder()
        .label("File")
        .submenu(&file_menu)
        .build();
    menu_bar.append(&file_menu_item);

    /* -------------------------------------------------------------------------- */
    /*                                  Edit Menu                                 */
    /* -------------------------------------------------------------------------- */
    let edit_menu = build_edit_menu();
    let edit_menu_item = gtk::MenuItem::builder()
        .label("Edit")
        .submenu(&edit_menu)
        .build();
    menu_bar.append(&edit_menu_item);

    /* -------------------------------------------------------------------------- */
    /*                                  Help Menu                                 */
    /* -------------------------------------------------------------------------- */
    let help_menu = build_help_menu();
    let help_menu_item = gtk::MenuItem::builder()
        .label("Help")
        .submenu(&help_menu)
        .build();
    menu_bar.append(&help_menu_item);
    /* -------------------------------------------------------------------------- */
    menu_bar
}

fn main() {
    let application = Application::builder()
        .application_id("org.ncc.mp3player")
        .build();
    application.connect_activate(|app| {
        let window: ApplicationWindow = ApplicationWindow::builder()
            .application(app)
            .title("MP3 Player")
            .default_width(800)
            .default_height(600)
            .build();

        let header = HeaderBar::builder()
            .title("MP3 Player")
            .show_close_button(true)
            .build();

        let menu_bar = build_menu(app.clone());
        header.pack_start(&menu_bar);
        window.set_titlebar(Some(&header));
        let main_box = gtk::Box::new(gtk::Orientation::Vertical, 0);
        main_box.add(&gtk::Label::new(Some("Hello, world!")));
        window.set_child(Some(&main_box));

        window.show_all();
    });

    application.run();
}
