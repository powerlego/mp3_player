use std::cell::RefCell;

use gio::prelude::Cast;
use gtk::glib;
use gtk::subclass::prelude::*;
use gtk::traits::WidgetExt;

#[derive(Default)]
pub struct ShuffleButton {
    child: RefCell<Option<gtk::Widget>>,
}

#[glib::object_subclass]
impl ObjectSubclass for ShuffleButton {
    const NAME: &'static str = "ShuffleButton";
    type Type = super::ShuffleButton;
    type ParentType = gtk::Widget;

    fn class_init(klass: &mut Self::Class) {
        klass.set_layout_manager_type::<gtk::BoxLayout>();
        klass.set_css_name("shufflebutton");
    }
}

impl ObjectImpl for ShuffleButton {
    fn constructed(&self) {
        self.parent_constructed();
        let obj = self.obj();

        let button = gtk::Button::new();
        button.add_css_class("shuffle-button");
        *self.child.borrow_mut() = Some(button.clone().upcast::<gtk::Widget>());

        button.set_parent(&*obj);
        obj.set_halign(gtk::Align::Center);
        obj.set_valign(gtk::Align::Center);
    }

    fn dispose(&self) {
        if let Some(child) = self.child.borrow_mut().take() {
            child.unparent();
        }
    }
}

impl WidgetImpl for ShuffleButton {}
impl ButtonImpl for ShuffleButton {}
