use std::cell::RefCell;

use gio::prelude::Cast;
use gtk::glib;
use gtk::subclass::prelude::*;
use gtk::traits::WidgetExt;

#[derive(Default)]
pub struct PlayButton {
    frame: RefCell<Option<gtk::AspectFrame>>,
    child: RefCell<Option<gtk::Widget>>,
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

        let button = gtk::Button::new();
        button.add_css_class("play-button");
        *self.child.borrow_mut() = Some(button.clone().upcast::<gtk::Widget>());

        let frame = gtk::AspectFrame::new(0.5, 0.5, 1.0, false);
        frame.set_valign(gtk::Align::Center);
        frame.set_halign(gtk::Align::Center);
        frame.set_parent(&*obj);
        frame.set_child(Some(&button));
        *self.frame.borrow_mut() = Some(frame.clone());
        obj.set_halign(gtk::Align::Center);
        obj.set_valign(gtk::Align::Center);
    }

    fn dispose(&self) {
        if let Some(frame) = self.frame.borrow_mut().take() {
            frame.unparent();
        }
    }
}
impl WidgetImpl for PlayButton {}
impl ButtonImpl for PlayButton {}
