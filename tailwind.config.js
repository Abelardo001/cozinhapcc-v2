module.exports = {
  content: [
    './core/templates/**/*.html',
    './template/**/*.HTML',
    './src/**/*.css'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#00a86b',
        secondary: '#ff7a00',
        'background-light': '#ffffff',
        'background-soft': '#f4f4f4',
        'text-main': '#333333',
        'text-muted': '#666666'
      },
      fontFamily: {
        display: ['Inter', 'sans-serif']
      },
      borderRadius: {
        DEFAULT: '8px',
        lg: '12px',
        xl: '16px',
        full: '9999px'
      }
    }
  },
  plugins: []
}
