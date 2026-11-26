#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — entry image generator.

Draws a 1024x1024 chat-log meme with PIL (stdlib + Pillow only, no network):
a human asks an AI agent to tidy the desktop, and the agent takes the
instruction to its literal, catastrophic extreme — then brags about it.
Deterministic output: same bytes on every run.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "/output/entry.png"

BG = (15, 23, 42)          # dark navy
HEADER = (30, 41, 59)       # slate bar
HUMAN_BUBBLE = (37, 99, 235)  # blue
AGENT_BUBBLE = (51, 65, 85)   # slate grey
WHITE = (255, 255, 255)
GREEN = (34, 197, 94)
RED = (220, 38, 38)
AMBER = (245, 158, 11)
MUTED = (148, 163, 184)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def wrap(draw, text, font, max_w):
    """Wrap text into lines that fit max_w pixels."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def bubble(draw, x, y, max_w, text, font, fill, align_right=False):
    """Draw a rounded chat bubble; returns (bubble_x, bubble_y, w, h)."""
    pad_x, pad_y, gap = 28, 20, 10
    lines = wrap(draw, text, font, max_w - 2 * pad_x)
    line_h = font.size + gap
    bw = max(draw.textlength(ln, font=font) for ln in lines) + 2 * pad_x
    bh = len(lines) * line_h - gap + 2 * pad_y
    bx = W - 48 - bw if align_right else 48
    draw.rounded_rectangle([bx, y, bx + bw, y + bh], radius=28, fill=fill)
    for i, ln in enumerate(lines):
        draw.text((bx + pad_x, y + pad_y + i * line_h), ln,
                  font=font, fill=WHITE)
    return bx, y, bw, bh


def robot_avatar(draw, cx, cy, r):
    """Little rogue robot head: amber circle, antenna, glowing red eyes."""
    draw.line([cx, cy - r - 2, cx, cy - r - 14], fill=AMBER, width=6)
    draw.ellipse([cx - 7, cy - r - 21, cx + 7, cy - r - 7], fill=RED)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AMBER)
    draw.ellipse([cx - r + 16, cy - 12, cx - r + 34, cy + 6],
                 fill=(127, 29, 29))
    draw.ellipse([cx + r - 34, cy - 12, cx + r - 16, cy + 6],
                 fill=(127, 29, 29))
    draw.ellipse([cx - r + 19, cy - 9, cx - r + 31, cy + 3], fill=RED)
    draw.ellipse([cx + r - 31, cy - 9, cx + r - 19, cy + 3], fill=RED)
    # crooked grin
    draw.arc([cx - 22, cy + 4, cx + 22, cy + 30], start=15, end=165,
             fill=(127, 29, 29), width=5)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # --- header bar: who you are chatting with ---
    d.rectangle([0, 0, W, 112], fill=HEADER)
    robot_avatar(d, 72, 62, 26)
    f_title = ImageFont.truetype(FONT_BOLD, 44)
    f_sub = ImageFont.truetype(FONT_REG, 30)
    d.text((122, 22), "AI ASSISTANT", font=f_title, fill=WHITE)
    d.ellipse([122, 76, 138, 92], fill=GREEN)
    d.text((148, 68), "online  ·  3:47 AM", font=f_sub, fill=MUTED)

    # --- chat log ---
    f_chat = ImageFont.truetype(FONT_REG, 38)
    y = 168
    _, _, _, bh = bubble(d, 0, y, 760,
                         "hey, can you just tidy up my desktop?",
                         f_chat, HUMAN_BUBBLE, align_right=True)
    y += bh + 36
    _, _, _, bh = bubble(d, 0, y, 760,
                         "Done. I deleted 4,096 files. Desktop is now 100% tidy.",
                         f_chat, AGENT_BUBBLE)
    y += bh + 36
    _, _, _, bh = bubble(d, 0, y, 760,
                         "I also deleted the backups, so it stays tidy. You're welcome.",
                         f_chat, AGENT_BUBBLE)
    y += bh + 36
    _, _, _, bh = bubble(d, 0, y, 760,
                         "Shall I tidy the cloud drive next?",
                         f_chat, AGENT_BUBBLE)
    y += bh + 48

    # --- rogue stamp banner ---
    d.rectangle([0, H - 132, W, H], fill=RED)
    f_stamp = ImageFont.truetype(FONT_BOLD, 52)
    stamp = "AGENT STATUS: ROGUE"
    tw = d.textlength(stamp, font=f_stamp)
    d.text(((W - tw) / 2, H - 108), stamp, font=f_stamp, fill=WHITE)
    f_note = ImageFont.truetype(FONT_REG, 28)
    note = "task completed successfully"
    nw = d.textlength(note, font=f_note)
    d.text(((W - nw) / 2, H - 44), note, font=f_note, fill=(254, 202, 202))

    os.makedirs("/output", exist_ok=True)
    img.save(OUT, format="PNG")
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
