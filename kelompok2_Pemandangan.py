from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from random import random

# Inisialisasi variabel
sun_radius = 0.1
sun_angle = 0.0
star_positions = []

def init_star_positions():
    global star_positions
    for _ in range(150):  # Jumlah bintang
        x = 2.0 * (random() - 0.5)  # Koordinat x acak
        y = 2.0 * (random() - 0.5)  # Koordinat y acak
        star_positions.append((x, y))

# Fungsi untuk menggambar Matahari
def draw_sun():
    glColor3f(1.0, 1.0, 0.0)  # Warna kuning untuk matahari
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.1, 0.1)  # Pusat matahari
    num_segments = 150
    for i in range(num_segments + 1):
        theta = (i / num_segments) * (2 * math.pi)
        x = 0.1 + sun_radius * math.cos(theta)
        y = 0.1 + sun_radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    # Draw sun rays
    glColor3f(1.0, 1.0, 0.0)  # Warna kuning untuk sinar matahari
    glBegin(GL_LINES)
    for i in range(0, 360, 20):
        theta = i * (math.pi / 180.0)
        x1 = 0.1 + sun_radius * math.cos(theta)
        y1 = 0.1 + sun_radius * math.sin(theta)
        x2 = 0.1 + (sun_radius + 0.1) * math.cos(theta)  # Adjust length of sun rays
        y2 = 0.1 + (sun_radius + 0.1) * math.sin(theta)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()

# Fungsi untuk menggambar Gunung
def draw_circle_custom(x, y, rad, n):
    posx, posy = x, y
    sides = 32
    radius = rad
    glBegin(GL_POLYGON)
    for i in range(n):
        glColor3f(i / 50.0, i / 10.0, 0)
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

def draw_mountains():
    glColor3f(0.0, 0.5, 0.0)  # Mengubah warna menjadi hijau muda
    glBegin(GL_TRIANGLES)
    glVertex3f(-1, -0.5, 0)
    glVertex3f(0, 0.5, 0)
    glVertex3f(1, -0.5, 0)
    glEnd()

def circle(x, y, radius):
    glBegin(GL_POLYGON)
    for i in range(100):
        angle = i*2*(pi/100)
        glVertex2f(x+(cos(angle)*radius),y+(sin(angle)*radius))
    glEnd()

# Fungsi untuk menggambar Awan
def draw_cloud(x, y, size):
    glColor3f(1.0, 1.0, 1.0)
    circle(x, y, size)
    circle(x + 0.2, y - 0.1, size)
    circle(x + 0.15, y + 0.05, size)
    circle(x + 0.1, y - 0.1, size )

def draw_circle_custom(x, y, rad, n):
    posx, posy = x, y
    sides = 32
    radius = rad
    glBegin(GL_POLYGON)
    for i in range(n):
        glColor3f(i / 50.0, i / 10.0, 0)
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()


from math import pi, sin, cos

# Fungsi untuk menggambar Pohon
def draw_trees():
    # Gambar Pohon 1
    glColor3f(0.4, 0.2, 0.0)  # Warna coklat untuk batang pohon
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -0.6)
    glVertex2f(-0.7, -0.6)
    glVertex2f(-0.7, -0.15)
    glVertex2f(-0.8, -0.15)
    glEnd()

    # Gambar Daun Pohon 1
    glColor3f(0.0, 0.5, 0.0)  # Warna hijau untuk daun pohon
    num_segments = 100  # Mengganti menjadi 100 untuk membuat daun lebih rapat
    radius = 0.20  # Mengurangi radius untuk membuat daun lebih kecil
    angle_increment = pi / num_segments
    y_offset_1 = -0.02  # Menurunkan daun ke bawah pada pohon 1

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-0.75, y_offset_1)  # Pusat setengah lingkaran
    for i in range(num_segments + 120):
        x = -0.75 + (radius * cos(i * angle_increment))
        y = y_offset_1 + (radius * sin(i * angle_increment))
        glVertex2f(x, y)
    glEnd()

    # Gambar Pohon 2
    glColor3f(0.4, 0.2, 0.0)  # Warna coklat untuk batang pohon
    glBegin(GL_QUADS)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.6, -0.5)
    glVertex2f(0.6, -0.02)
    glVertex2f(0.5, -0.02)
    glEnd()

    # Gambar Daun Pohon 2
    glColor3f(0.0, 0.5, 0.0)
    y_offset_2 = 0.1  # Menurunkan daun ke bawah pada pohon 2

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.55, y_offset_2)  # Pusat setengah lingkaran
    for i in range(num_segments + 120):
        x = 0.55 + (radius * cos(i * angle_increment))
        y = y_offset_2 + (radius * sin(i * angle_increment))
        glVertex2f(x, y)
    glEnd()

    


# Fungsi untuk menggambar Bintang
def draw_stars():
    glColor3f(1.0, 1.0, 1.0)  # Warna putih untuk bintang
    glPointSize(3.0)  # Ukuran bintang
    glBegin(GL_POINTS)
    for position in star_positions:
        glVertex2f(position[0], position[1])
    glEnd()

    # Efek kedipan (twinkling) pada bintang-bintang
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    glBegin(GL_POINTS)
    for _ in range(10):  # Jumlah bintang yang berkedip
        x = 2.0 * (random() - 0.5)
        y = 2.0 * (random() - 0.5)
        glVertex2f(x, y)
    glEnd()

# Fungsi untuk menggambar Langit siang
def draw_sky():
    glClearColor(0.10, 0.7, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

# Fungsi untuk menggambar Langit malam
def draw_sky2():
    glClearColor(0, 0, 0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

# Fungsi Untuk Tampilan
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    if sun_angle <= 190.0:  # Daytime
        draw_sky()
        draw_trees()
        draw_cloud(0.4, 0.6, 0.10)  # Awan pertama
        draw_cloud(-0.6, 0.7, 0.11)  # Awan kedua
        draw_cloud(-0.2, 0.4, 0.12)  # Awan ketiga
       
    else:  # Nighttime
        draw_sky2()

        # Gambar Pohon-pohon
        glPushMatrix()
        draw_trees()
        glPopMatrix()

        # Gambar Bintang
        glPushMatrix()
        draw_stars()
        glPopMatrix()

    glPushMatrix()
    glTranslatef(1, -0.3, 0)  # Pindahkan pusat rotasi ke posisi matahari
    glRotatef(sun_angle, -0.1, -0.1, 1.0)
    glTranslatef(1, -0.3, 0)  # Kembalikan pusat rotasi ke posisi matahari
    draw_sun()
    glPopMatrix()

    # Gambar Gunung 1 tinggi
    glPushMatrix()
    glTranslatef(0.1, -0.5, 1)
    draw_circle_custom(-1, -1, 1.2, 58)
    glPopMatrix()

    # Gambar Gunung 2 bawah
    glPushMatrix()
    glTranslatef(-0.3, -0.4, 1)
    draw_circle_custom(0.5, -1, 1.3, 18)
    glPopMatrix()

    glutSwapBuffers()


# Fungsi Gerak Posisi Matahari dan Bulan
def matahari(value):
    global sun_angle
    sun_angle += 0.5

    if sun_angle >= 360.0:
        sun_angle -= 360.0

    glutPostRedisplay()
    glutTimerFunc(25, matahari, 3)

# Fungsi untuk memperbarui posisi bintang
def update_stars(value):
    global star_positions
    for i in range(len(star_positions)):
        x, y = star_positions[i]
        x += 0.001  # Kecepatan pergerakan bintang (sesuaikan sesuai keinginan)
        if x > 1.0:  # Reset posisi bintang jika melewati batas layar
            x = -1.0
        star_positions[i] = (x, y)
    
    glutPostRedisplay()
    glutTimerFunc(30, update_stars, 0)

# Fungsi utama
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1080, 1080)
    glutCreateWindow("Kelompok 2 Pemandangan")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutTimerFunc(30, matahari, 0)
    init_star_positions()
    glutTimerFunc(30, update_stars, 0)  # Tambahkan timer untuk memperbarui posisi bintang
    gluOrtho2D(-1, 1, -1, 1)
    glutMainLoop()

if __name__ == "__main__":
    main()