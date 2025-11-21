# Troubleshooting Guide

## Issue: Content Overflows Presentation Slide

**Symptoms:**
- Text cut off at bottom of slide
- Scroll bar appears in browser
- Print output truncated

**Solutions:**
1. **Reduce text length**: Tighten descriptions, use bullet points
2. **Move detailed content**: Use executive format for lengthy content
3. **Split content**: Request modification to split into two slides (advanced)
4. **Adjust font size**: Reduce specific section font (advanced customization)

**Prevention:**
- Keep metric descriptions under 20 words
- Limit momentum highlights to 3-4 items
- Use concise outcome titles (under 10 words)
- Test presentation format with longest content first

---

## Issue: Brand Color Not Displaying

**Symptoms:**
- Default orange color appears instead of specified color
- Color looks wrong or unexpected
- Inconsistent color application

**Solutions:**
1. **Verify hex format**: Ensure format is exactly `#RRGGBB` (e.g., `#0052CC`)
2. **Check CSS variables**: Confirm `--brand-color` updated in both templates
3. **Clear browser cache**: Hard refresh (Cmd+Shift+R or Ctrl+Shift+R)
4. **Validate color code**: Use color picker to verify valid hex

**Prevention:**
- Always include `#` prefix
- Use 6-character hex codes (not 3-character shorthand)
- Test color in small sample before full generation
- Use recommended sector colors for safety

---

## Issue: Navigation Broken or Skipping Slides

**Symptoms:**
- Arrow keys don't advance slides
- Dots navigation jumps incorrectly
- Keyboard shortcuts don't work

**Solutions:**
1. **Verify slide attributes**: Check `data-slide` attributes are sequential (0,1,2,3,4,5,6)
2. **Check JavaScript console**: Look for errors in browser developer tools
3. **Test in different browser**: Try Chrome if using Firefox/Safari
4. **Regenerate file**: Request fresh generation if corruption suspected

**Prevention:**
- Always test navigation before distribution
- Use recommended browsers (Chrome/Edge)
- Don't manually edit HTML unless experienced

---

## Issue: Print Layout Incorrect

**Symptoms:**
- Multiple slides per page
- Wrong orientation
- Background colors missing
- Text cut off

**Solutions:**
1. **Use Chrome browser**: Most consistent print rendering
2. **Verify orientation**: Landscape for presentation, portrait for executive
3. **Enable background graphics**: Required for colors and design
4. **Check margins**: Set to "None" for full-bleed design
5. **Preview before saving**: Use print preview to check

**Prevention:**
- Always use Chrome for PDF export
- Follow exact export instructions
- Test print preview before saving
- Save print settings as default in Chrome

---

## Issue: Content Not Aligned Across Formats

**Symptoms:**
- Presentation format has different content than executive
- Sections don't match between formats
- Missing content in one format

**Solutions:**
1. **Verify content schema**: Ensure all fields populated correctly
2. **Check template population**: Request regeneration with verified content
3. **Review validation**: Confirm both formats passed QA

**Prevention:**
- Use single content source for both formats
- Validate content schema before generation
- Test both formats after generation

---

## Issue: Mobile Display Problems

**Symptoms:**
- Layout broken on phone/tablet
- Text too small or overlapping
- Navigation not functional on mobile

**Solutions:**
1. **Test responsive breakpoints**: Resize browser to test
2. **Verify viewport meta tag**: Should be present in HTML head
3. **Check touch targets**: Navigation elements should be tappable
4. **Simplify complex tables**: Some tables may need mobile-specific layout

**Prevention:**
- Test on actual mobile device before distribution
- Keep content simple for mobile viewing
- Understand mobile is secondary (desktop-first design)
- Consider executive format for mobile (better for scrolling)
