use gtk::prelude::*;
use gtk::{Application, ApplicationWindow};

fn build_file_menu (app: Application) -> gtk::Menu {
    let menu = gtk::Menu::new();
    let new_playlist = gtk::MenuItem::new();
    new_playlist.set_label("New Playlist");
    new_playlist.connect_activate(|_| {
        println!("New Playlist");
    });
    menu.append(&new_playlist);
    let open = gtk::MenuItem::new();
    open.set_label("Open");
    menu.append(&open);
    let separator = gtk::SeparatorMenuItem::new();
    menu.append(&separator);
    let quit = gtk::MenuItem::new();
    quit.set_label("Quit");
    quit.connect_activate(move |_| {
        app.quit();
    });
    menu.append(&quit);
    menu
}

fn build_menu(app: Application) -> gtk::MenuBar {
    let menu_bar = gtk::MenuBar::new();
    let file_menu = build_file_menu(app);
    let file_menu_item = gtk::MenuItem::new();
    file_menu_item.set_label("File");
    file_menu_item.set_submenu(Some(&file_menu));
    menu_bar.append(&file_menu_item);
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

        let main_box = gtk::Box::new(gtk::Orientation::Vertical, 0);
        let menu_bar = build_menu(app.clone());
        main_box.pack_start(&menu_bar,false, false, 0);
        main_box.add(&gtk::Label::new(Some("Hello, world!")));
        window.set_child(Some(&main_box));
        
        window.show_all();
    });

    application.run();
}
