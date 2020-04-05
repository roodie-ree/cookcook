import { Link, RouteComponentProps } from '@reach/router'
import React, { ReactElement } from 'react'

function RecipesPage (props: RouteComponentProps): ReactElement {
  return (
    <Link to='/'>Start Page</Link>
  )
}

export { RecipesPage }
