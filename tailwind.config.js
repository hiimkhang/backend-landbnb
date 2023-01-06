/** @type {import('tailwindcss').Config} */
module.exports = {
  content: {
    relative: true,
    files: [
      './templates/*.{html, js}',
      './templates/**/*.{html, js}',
    ]
  },
  theme: {
    extend: {},
  },
  plugins: [],
}
