use gtk::prelude::*;
use gtk::{gio, glib, Application, ApplicationWindow};

fn build_file_menu() -> gio::Menu {
    let menu = gio::Menu::new();
    menu.append(Some("New Playlist"), Some("app.new.playlist"));
    menu.append(Some("Open"), Some("app.open"));
    let io = gio::Menu::new();
    let import = gio::Menu::new();
    import.append(Some("File"), Some("app.import.file"));
    import.append(Some("Folder"), Some("app.import.folder"));
    import.append(Some("Playlist"), Some("app.import.playlist"));
    io.append_submenu(Some("Import"), &import);
    io.append(Some("Export"), Some("app.export"));
    menu.append_section(None, &io);
    let quit = gio::Menu::new();
    quit.append(Some("Quit"), Some("app.quit"));
    menu.append_section(None, &quit);
    menu
}

fn build_menu(app: &gtk::Application) {
    let menu = gio::Menu::new();
    let file_menu = build_file_menu();
    menu.append_submenu(Some("File"), &file_menu);
    app.set_menubar(Some(&menu));
}

fn add_accelerators(app: &gtk::Application) {
    app.set_accels_for_action("app.open", &["<Primary>O"]);
    app.set_accels_for_action("app.new.playlist", &["<Primary>N"]);
    app.set_accels_for_action("app.quit", &["<Primary>Q"]);
}

fn add_actions(app: &gtk::Application, window: &gtk::ApplicationWindow) {
    let open = gio::SimpleAction::new("open", None);
    open.connect_activate(|_, _| {
        println!("Open");
    });
    app.add_action(&open);
    let quit = gio::SimpleAction::new("quit", None);
    quit.connect_activate(glib::clone!(@weak window => move |_, _| {
        window.close();
    }));
    app.add_action(&quit);

    let new_playlist = gio::SimpleAction::new("new.playlist", None);
    new_playlist.connect_activate(|_, _| {
        println!("New Playlist");
    });
    app.add_action(&new_playlist);

    let import_file = gio::SimpleAction::new("import.file", None);
    import_file.connect_activate(|_, _| {
        println!("Import File");
    });
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
    let label = gtk::Label::new(Some("MP3 Player"));
    vbox.append(&label);
    window.set_child(Some(&vbox));

    build_menu(app);

    add_actions(app, &window);

    window.show();
}

fn main() {
    let application = Application::builder()
        .application_id("org.ncc.mp3player")
        .build();

    application.connect_startup(|app| {
        add_accelerators(app);
    });

    application.connect_activate(build_ui);

    application.run();
}
