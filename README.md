## About

Raytracer in Python written using [*The Raytracer Challenge*](http://raytracerchallenge.com/) (I highly recommend checking it out! One of my favorite nonfiction books.) The book takes you through writing the code for a raytracer using test-driven development. 

I'll summarize how it works as explained in the book. Basically, it uses an algorithm known as *Whitted ray tracing*, which works by "recursively spawning rays (lines representing rays of light) and bouncing them around the scene to discover what color each pixel of the final image should be". According to the book, the steps to this algorithm are:

1. Cast a ray onto the scene, and find where it strikes a surface.
2. Cast a ray from that point toward each light source to determine where lights illuminate that point.
3. If the surface is reflective, cast a new ray in the direction of reflection and recursively determine what color is reflected there.
4. If the surface is transparent, do the same thing in the direction of refraction.
5. Combine all colors that contribute to the point (the color of the surface, the reflection, and refraction) and return that as the color of the pixel.

The unit tests are written with `unittest`, replacing the ones in the book which are written with [Cucumber](https://cucumber.io/).

### Name?

Oh yeah, I'm getting into naming my projects the weirdest names possible. Although I promise you there's logic behind every single one! For this one, a prancer is a fiery horse, and is also a nice combination of Python, ray, and tracer.

### Example renders

After going through the book, the first thing I did was render a desktop background for myself! LOL.

## Thoughts

* This is the most fucking detailed code I have written. More comments than LOC.
* I have to package it to use relative imports? NPM sucks with dependencies but you don't have to deal with this at least. Python environments are seriously confusing (not their usage, but e.g. the fact that Python and Anaconda both provide environment support of their own).
* **Regarding optimization**: I think I might write a version in NumPy for the vectorization benefits and also to learn NumPy? Multithreading would also be something interesting to take a look at, in addition to OpenGL (using GPU instead of CPU, although a different file format would have to be used). Wait, isn't this literally what a shader does? LOL

## Going through the book

* Implementing tuples, vectors, and points, which are basically variations on one another
* Implementing colors