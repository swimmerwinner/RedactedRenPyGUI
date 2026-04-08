init offset = -1

################################################################################
## Basics
################################################################################

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language
define gui.language = "unicode"





################################################################################
## Common Values
################################################################################

## Dialogue and choices text.
define gui.dialogue_color = '#ffffff'
define gui.dialogue_font = "AtkinsonHyperlegible"
define gui.dialogue_size = 33

# Character name text.
define gui.name_color = '#0099cc'
define gui.name_font = "AtkinsonHyperlegible"
define gui.name_size = 45

## UI normal text.
define gui.ui_text_color = '#ffffff'
define gui.ui_text_font = "AtkinsonHyperlegible"
define gui.ui_text_size = 33

## UI accents.
define gui.accent_color = '#0099cc'
define gui.label_font = "AtkinsonHyperlegible"
define gui.label_size = 36

## Button text colors.
define gui.button_idle_color = '#888888'
define gui.button_hover_color = '#66c1e0'
define gui.button_selected_color = '#ffffff'
define gui.button_insensitive_color = '#8888887f'





################################################################################
## Default Styles
################################################################################

# style default:
#     properties gui.text_properties()
#     language gui.language

# style input:
#     properties gui.text_properties("input", accent=True)
#     adjust_spacing False

# style hyperlink_text:
#     properties gui.text_properties("hyperlink", accent=True)
#     hover_underline True

# style gui_text:
#     properties gui.text_properties("interface")


# style button:
#     properties gui.button_properties("button")

# style button_text is gui_text:
#     properties gui.text_properties("button")
#     yalign 0.5


# style label_text is gui_text:
#     properties gui.text_properties("label", accent=True)

# style prompt_text is gui_text:
#     properties gui.text_properties("prompt")
