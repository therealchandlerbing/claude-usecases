/**
 * Vite configuration for building standalone HTML version
 *
 * This config generates a single HTML file with embedded CSS and JS
 * for easy distribution and viewing without a build pipeline.
 *
 * Usage: npm run build:standalone
 * Output: dist/standalone/index.html
 */

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist/standalone',
    // Inline all assets into the HTML
    assetsInlineLimit: 100000000, // High limit to inline everything
    cssCodeSplit: false,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
      },
      output: {
        // Single JS file
        entryFileNames: 'assets/[name].js',
        chunkFileNames: 'assets/[name].js',
        assetFileNames: 'assets/[name].[ext]',
        // Attempt to inline as much as possible
        inlineDynamicImports: true,
      },
    },
    // Minify for smaller file size
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: false, // Keep console for debugging
      },
    },
  },
  // Base path for assets
  base: './',
  resolve: {
    alias: {
      '@': resolve(__dirname, './src'),
    },
  },
})
