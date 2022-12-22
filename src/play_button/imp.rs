use std::cell::RefCell;

use gdk_pixbuf::prelude::*;
use gtk::glib;
use gtk::prelude::*;
use gtk::subclass::prelude::*;
use gtk::traits::WidgetExt;

#[derive(Default)]
pub struct PlayButton {
    frame: RefCell<Option<gtk::AspectFrame>>,
    child: RefCell<Option<gtk::Widget>>,
    pub playing: RefCell<bool>,
}

#[glib::object_subclass]
impl ObjectSubclass for PlayButton {
    const NAME: &'static str = "PlayButton";
    type Type = super::PlayButton;
    type ParentType = gtk::Widget;

    fn class_init(klass: &mut Self::Class) {
        klass.set_layout_manager_type::<gtk::BoxLayout>();
        klass.set_css_name("playbutton");
    }
}

impl ObjectImpl for PlayButton {
    fn constructed(&self) {
        self.parent_constructed();
        let obj = self.obj();
        let button: gtk::Button = gtk::Button::new();
        button.add_css_class("play-button");
        let frame = gtk::AspectFrame::new(0.5, 0.5, 1.0, false);
        frame.set_parent(&*obj);
        *self.frame.borrow_mut() = Some(frame.clone());
        frame.set_child(Some(&button));
        // let file = gio::File::for_path("resource:///org/ncc/mp3player/images/play_button.svg");
        // let stream = file.read(None::<&gio::Cancellable>).unwrap();
        // let handle = librsvg::Loader::new().read_stream(&stream, Some(&file), None::<&gio::Cancellable>).unwrap();
        // let surface = cairo::ImageSurface::create(cairo::Format::ARgb32, 100, 100).unwrap();
        // let cr = cairo::Context::new(&surface).unwrap();

        // let renderer = librsvg::CairoRenderer::new(&handle);
        // renderer.render_document(&cr, &cairo::Rectangle::new(0.0, 0.0, 100.0, 100.0));
        
        
        // let icon = gtk::Image::from_icon_name("play-button-symbolic");
        // icon.add_css_class("play-button-icon");

        // button.set_child(Some(&icon));
        let icon = gtk::Image::from_icon_name("play-button-symbolic");
        button.set_child(Some(&icon));
        
        // icon.set_halign(gtk::Align::Fill);
        // icon.set_valign(gtk::Align::Fill);
        //icon.set_icon_size(gtk::IconSize::Large);
        button.connect_clicked(|button| {
            let play_button = button
                .parent()
                .unwrap()
                .parent()
                .unwrap()
                .downcast::<super::PlayButton>()
                .unwrap();
            let imp = play_button.imp();
            let mut playing = imp.playing.borrow_mut();
            if *playing {
                button.remove_css_class("playing");
                
            } else {
                button.add_css_class("playing");
                
            }
            *playing = !*playing;
            println!("{:?}", button.size(gtk::Orientation::Horizontal));
        });
        *self.child.borrow_mut() = Some(button.clone().upcast::<gtk::Widget>());
        obj.set_halign(gtk::Align::Center);
        obj.set_valign(gtk::Align::Center);
    }

    fn dispose(&self) {
        // if let Some(child) = self.child.borrow_mut().take() {
        //     child.unparent();
        // }
        if let Some(frame) = self.frame.borrow_mut().take() {
            frame.unparent();
        }
    }
}
impl WidgetImpl for PlayButton {}
impl ButtonImpl for PlayButton {}
