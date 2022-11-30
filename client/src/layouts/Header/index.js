import React from 'react'
import { Link } from 'react-router-dom'

export default function Header() {
  const activeClass = ({isActive}) => isActive ? 'current' : undefined
  return (
    <ul>
      <li NavLink className={activeClass}> <Link to="/">Home</Link></li>
    </ul>
  )
}
