import { BottomAppBar } from '../layouts/BottomAppBar'
import { cookcookTheme } from './Theme'
import { RecipesPage } from '../pages/RecipesPage'
import { Router } from '@reach/router'
import { StartPage } from '../pages/StartPage'
import { Container, CssBaseline, ThemeProvider } from '@material-ui/core'
import React, { ReactElement } from 'react'

import '@openfonts/fira-sans_latin'

function Root (): ReactElement {
  return (
    <ThemeProvider theme={ cookcookTheme }>
      <CssBaseline />
      <Container maxWidth='lg'>
        <Router>
          <StartPage path='/' />
          <RecipesPage path='/recipes' />
        </Router>
        <BottomAppBar />
      </Container>
    </ThemeProvider>
  )
}

export { Root }
