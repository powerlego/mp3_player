use gtk::prelude::*;
use gtk::{Application, ApplicationWindow, gio, glib};

fn build_menu(app: &gtk::Application) {
    let menu = gio::Menu::new();
    let file_menu = gio::Menu::new();
    file_menu.append(Some("Open"), Some("app.open"));
    file_menu.append(Some("Quit"), Some("app.quit"));
    menu.append_submenu(Some("File"), &file_menu);
    app.set_menubar(Some(&menu));
}

fn add_accelerators(app: &gtk::Application) {
    app.set_accels_for_action("app.open", &["<Primary>O"]);
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
