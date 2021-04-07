#include "GUI.h"
#include "includes.h"
#include "background.h"

void LCD_SetWindow(uint16_t sx, uint16_t sy, uint16_t ex, uint16_t ey)
{
  LCD_WR_REG(0x2A);
  LCD_WR_DATA(sx>>8);LCD_WR_DATA(sx&0xFF);
  LCD_WR_DATA(ex>>8);LCD_WR_DATA(ex&0xFF);
  LCD_WR_REG(0x2B);
  LCD_WR_DATA(sy>>8);LCD_WR_DATA(sy&0xFF);
  LCD_WR_DATA(ey>>8);LCD_WR_DATA(ey&0xFF);
}

void GUI_Clear()
{
  GUI_FillRectColor(0, 0, LCD_WIDTH, LCD_HEIGHT, LCD_COLOR_BACKGROUND);
}

void GUI_FillRectColor(uint16_t sx, uint16_t sy, uint16_t ex, uint16_t ey, uint16_t color)
{
  uint32_t x=0, y=0;
  LCD_SetWindow(sx, sy, ex-1, ey-1);
  LCD_WR_REG(0x2C);
  for(y=sy; y<ey; y++)
  {
    for(x=sx; x<ex; x++)
    {
      if (color == LCD_COLOR_BACKGROUND) {
        LCD_WR_16BITS_DATA(backgroundPalette[backgroundPixels[y][x]]);
      } else {
        LCD_WR_16BITS_DATA(color);
      }
    }
  }
}
