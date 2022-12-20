use gtk::glib;

mod imp;

glib::wrapper! {
    pub struct ShuffleButton(ObjectSubclass<imp::ShuffleButton>) @extends gtk::Button, gtk::Widget, @implements gtk::Accessible, gtk::Actionable,
                    gtk::Buildable, gtk::ConstraintTarget;

}

impl ShuffleButton {
    pub fn new() -> Self {
        glib::Object::new(&[])
    }
}

impl Default for ShuffleButton {
    fn default() -> Self {
        Self::new()
    }
}