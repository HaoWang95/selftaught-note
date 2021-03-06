# **Material UI**

To use material ui, first install the dependencies in a React app.

> - npm install @material-ui/core or yarn add @material-ui/core
> - npm install @material-ui/styles or yarn add @material-ui/styles

## Theming

To customize the theme, we need a **ThemeProvider** component to inject a theme into our app.
_Note: Material ui components come with a default theme._

The default theme object exploration:

- breakpoints: Object
  - keys: Array(5) -> xs sm md lg xl
  - vavlues: Object xs 0 sm 600 md 960 lg 1280 xl 1920 -> the size
  - up: function d()
  - down function down()
  - between: f p()
  - only: f only()
  - width: f width()
  - direction: "ltr"
- mixins: Object
  - gutters: f gutters()
  - toolbar: Object
    - minHeight: 56
    - two @media object with minHeight attribute
- overrides: Object
- palette: Object
  - common: Object
    - black: #000
    - white: #fff
  - type: "light"
  - primary: Object
    - light: light color value #7986cb
    - main: main color value #3f51b5
    - dark: dark color value #303f9f
    - contrastText: #fff
  - secondary: Object
    - Attributes same as primary, but color values are different
  - error: Object
    - Attributes same as primary and secondary, but color values are different
  - warning: Object
    - Attributes same as above, but color values are different
  - info: Object
    - Attributes same as above, but color values are different
  - success: Object
    - Attributes same as above, but color values are different
  - grey: Object
    - value from 50 to A700
  - contrastThreshold: 3
  - getContrastText: f E()
  - augmentColor: f l()
  - tonalOffset: 0.2
  - text: Object all text color are displayed as rgba value
    - primary
    - secondary
    - disabled
    - hint
  - background: Object
    - paper: #fff
    - default: #fafafa
  - action: Object
    - active
    - hover
    - hoverOpacity
    - selected
    - selectedOpacity
    - disabled
    - disabledBackground
    - disabledOpacity
    - focus
    - focusOpacity
    - activatedOpacity
  - props: Object
- shadows: Array(25)
  - index from 0-24 for shadow value
- typography: Object
  - htmlFontSize: 16
  - pxToRem: f()
  - round: f T()
  - fontFamily: ""Roboto", "Helvetica", "Arial", sans-serif"
  - fontSize: 14
  - fontWeightLight: 300
  - fontWeightRegular: 400
  - fontWeightMedium: 500
  - fontWeightBold: 700
  - h1: Object
    - fontFamily: same as above
    - fontWeight: 300
    - fontSize: 6rem
    - lineHeight: 1.167
    - letterSpacing: a very werid value
  - h2: Object setting attributes same as h1
  - h3: Object setting attributes same as h1
  - h4: Object setting attributes same as h1
  - h5: Object setting attributes same as h1
  - h6: Object setting attributes same as h1
  - subtitle1: Object setting attributes same as h1
  - subtitle2: Object setting attributes same as h1
  - body1: Object setting attributes same as h1
  - body2: Object setting attributes same as h1
  - button: object
    - setting attributes same as h1
    - textTransform: "uppercase"
  - caption: Object setting attributes same as h1
  - overline: Object setting attributes same as _button_
- spacing: f e()
  - mui: true
- shape: Object
  - borderRadius: 4
- transitions: Object
  - easing: Object
    - easeInOut: "cubic-bezier(0.4, 0, 0.2, 1)"
    - easeOut: "cubic-bezier(0.0, 0, 0.2, 1)"
    - easeIn: "cubic-bezier(0.4, 0, 1, 1)"
    - sharp: "cubic-bezier(0.4, 0, 0.6, 1)"
  - duration: Object
    - shortest: 150
    - shorter: 200
    - short: 250
    - standard: 300
    - complex: 375
    - enteringScreen: 225
    - leavingScreen: 195
  - create f create()
  - getAutoHeightDuration: f getAutoHeightDuration()
- zIndex: Object
  - mobileStepper: 1000
  - speedDial: 1050
  - appBar: 1100
  - drawer: 1200
  - modal: 1300
  - snackbar: 1400
  - tooltip: 1500

Though there are tons of attributes provided by default theme in material ui. Common used attributes are mainly about palette and typography.

The API we can use to create a theme is **createTheme(options, ...args) => theme**

## Common settings in material ui and css

### **display: flex**

This is a common setting in a container. The container becomes flexible by setting the display property to flex. By default, it will be flexible horizontally.
Adding **flex-direction: column** to change it to be flexible vertically.

### Grid

In `MUI`, the grid system is implemented with the `Grid` component.

- **`CSS Flexible Box Module`** for high flexibility
- Two types of layout in MUI: `container` and `item`
- Five grid breakpoints: `xs` `sm` `md` `lg` and `xl`
- Integer values can be given to each break point, indicating how many of the 12 available columns are occupied by the component when the viewport width satisfies the breakpoint constraints.

> Basic grid
> Column widths are integer values between 1 and 12;
