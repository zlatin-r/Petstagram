class ReadOnlyFieldFormMixin:
    readonly_fields = ()

    def _apply_readonly_on_fields(self):
        for field_name in self.read_only_field_names:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"

    @property
    def read_only_field_names(self):
        if self.readonly_fields == "__all__":
            return self.fields.keys()

        return self.readonly_fields