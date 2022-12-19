use gtk::glib;

mod imp;

glib::wrapper! {
    pub struct PlayButton(ObjectSubclass<imp::PlayButton>) @extends gtk::Button, gtk::Widget, @implements gtk::Accessible, gtk::Actionable,
                    gtk::Buildable, gtk::ConstraintTarget;

}

impl PlayButton {
    pub fn new() -> Self {
        glib::Object::new(&[])
    }
}

impl Default for PlayButton {
    fn default() -> Self {
        Self::new()
    }
}
