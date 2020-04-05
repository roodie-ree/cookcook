import { Add, Menu, More, Search } from '@material-ui/icons'
import { AppBar, Fab, IconButton, Toolbar } from '@material-ui/core'
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles'
import React, { ReactElement } from 'react'

const useStyles = makeStyles((theme: Theme) => createStyles({
  appBar: {
    top: 'auto',
    left: 'auto',
    right: 'auto',
    bottom: 0,
    width: theme.breakpoints.width('lg'),
  },
  grow: {
    flexGrow: 1,
  },
  fabButton: {
    position: 'absolute',
    zIndex: 1,
    top: -30,
    left: 0,
    right: 0,
    margin: '0 auto',
  },
}))

function BottomAppBar (): ReactElement {
  const classes = useStyles()

  return (
    <AppBar position='fixed' color='primary' className={ classes.appBar }>
      <Toolbar>
        <IconButton edge='start' color='inherit' aria-label='open drawer'>
          <Menu />
        </IconButton>
        <Fab color='secondary' aria-label='add' className={ classes.fabButton }>
          <Add />
        </Fab>
        <div className={ classes.grow } />
        <IconButton color='inherit'>
          <Search />
        </IconButton>
        <IconButton edge='end' color='inherit'>
          <More />
        </IconButton>
      </Toolbar>
    </AppBar>
  )
}

export { BottomAppBar }
