import React from 'react'
import { Link } from 'react-router-dom'

export default function Header() {
  const activeClass = ({isActive}) => isActive ? 'current' : undefined
  return (
    <div>
      <p NavLink className={activeClass}> <Link to="/">Home</Link></p>
    </div>
  )
}
