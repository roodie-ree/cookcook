import { amber, blue, blueGrey, green, red } from '@material-ui/core/colors'
import { createMuiTheme, responsiveFontSizes } from '@material-ui/core/styles'

const cookcookTheme = responsiveFontSizes(createMuiTheme({
  palette: {
    primary: amber,
    secondary: blue,
    error: red,
    success: green,
    info: blueGrey,
  },
  typography: {
    fontFamily: '"Fira Sans", "Helvetica", "Arial", sans-serif',
  },
}))

export { cookcookTheme }
