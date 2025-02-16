// src\app\page.tsx

import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <header>
        <h1>Welcome to BlueHands</h1>
        <p>Bluehands is uses a Machine Learning Model in order to detect hand gestures, in order to control PC functions such as your mouse or volume!</p>
      </header>

      <section>
        <h2>About Us</h2>
        <p>
          This project was created to work on creating another input method in order to reduce typing, as it medically proven to cause carpal deformaties and pain. 
          We believe it will allow people to enjoy the web with ease... or simply eat snacks while watching a youtube video without getting a gunky keyboard.
        </p>
      </section>

      <section>
        <h2>Find Our Code</h2>
        <p>Check out our source code and contribute on GitHub:</p>
        <a href="https://github.com/NomadicCat/JakinCrimsonHack2025" target="_blank" rel="noopener noreferrer">
        Visit our GitHub Repository!
        <a/>
      </section>

      <footer>
        <p>© 2025 PineappleJamming. All Rights Reserved.</p>
      </footer>
    </div>
  )
}
