import { Link, RouteComponentProps } from '@reach/router'
import React, { ReactElement } from 'react'

function StartPage (props: RouteComponentProps): ReactElement {
  return (
    <Link to='recipes'>Recipes</Link>
  )
}

export { StartPage }
