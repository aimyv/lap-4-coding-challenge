import React, { useContext, useState } from 'react'

export default function Home() {

  const handleSubmit = event => {
    event.preventDefault();
    alert('URL SHRTND!')
  }

  return (
    <div>
      <h1>SH&#9988;RT&#9988;N&#9988;R</h1>
      <div>
        <form onSubmit={handleSubmit}>
          <label>
            <input type="text" longurl="longurl" />
            </label>
            <button type="submit">SHRTN!</button>
        </form>
      </div>
    </div>
  )
}
