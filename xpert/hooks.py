from . import __version__ as app_version

app_name = "xpert"
app_title = "Xpert"
app_publisher = "V"
app_description = "Xpert customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "moustafa.imym@gmail.com"
app_license = "MIT"


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"xpert.auth.validate"
# ]

fixtures = [
    {"dt": "DocType", "filters": [
        [
            "module", "in", [
                "Xpert"
            ]
        ]
    ]},
    "Web Form"
]
