Flexbox
#######

Flexboxes are first-class citizens in aircss to build advanced layouts. Their
use is made simple through an expressive set of dedicated classes to configure
the containers and their child items.

Create a container
==================

Creating a flexbox container only requires to add the ``flex`` class to an
element. All of its child elements will be laid along the main axis of the
newly created flexbox on one line or on multiple lines if the ``wrapped`` class
is added to it.

If no additional class is set, the flexbox will have a horizontal main axis as
if the additional class ``row`` has been specified. To create a flexbox
container with a vertical main axis the additional class ``column`` should be
used.

The default starting point on the main axis is on the left for a horizontal
flexbox and on the top for a vertical one. It is possible to set the starting
point respectively to the right and the botton with the use of the ``reverse``
additional class.

Finally, it is possible to distribute the child items along the main axis with
two different strategies: ``evenly-spaced`` or ``evenly-filled``. If no
strategy is set, the default behavior is to align items to the starting point. 


Configure child items
=====================

Flexbox child items can be configured to change how they fill the main axis and
how they position along the cross axis of their parent container.

Any element can shrink to its minimum allowed size to fit the main axis. The
use of the ``grow`` class allows an element to expand and fill the main axis.
Otherwise, it still possible to force an element to neither grow nor shrink by
adding the ``noflex`` class to it.

On the cross axis, the default behavior of a child item is to stretch across it
and fill the parent container. If it is not desired, the position of the child
item along the cross axis must be specified with the help of a class among
``start``, ``center`` or ``end``.


Syntax and classes
==================

Containers
----------

**Syntax:** ``[evenly-filled|evenly-spaced] [reverse] [wrapped] 
flex [row|column]``

**Default:** A flexbox container hass an horizontal main axis with child items
aligned to the starting point.

``flex``: create a flexbox container

``wrapped``: span child elements on multiple lines if they overflow the
container main axis length.

``row``: set the main axis horizontally *(implicit)*

``column``: set the main axis vertically

``reverse``: set the starting point to the right for an horizontal flexbox and
to the bottom for a vertical flexblox

``evenly-filled``: items will have equal space between them

``envenly-spaced``: items will have equal space around them


Child items
-----------

**Syntax:** ``[grow|noflex] [start|center|end]``

**Default:** An item will shrink to fit the main axis and stretch to fill the
cross axis. 

``grow``: An item will expand to fill the main axis

``noflex``: An item will neither grow nor shrink

``start``: The item is positioned at the start of the cross axis of the
container

``center``: The item is centered on the cross-axis of the container

``end``: The item is positioned at the end of the cross axis of the container


Examples
========

*To better illustrate the working of the flexboxes, the following examples use
a red border for the container and a black border for the child items. Some
padding is voluntarily added for the sake of clarity.*

This example show the default behavior of a flexbox container:

.. code:: html

    <div class="flex">
        <div>1 →</div>
        <div>2 →</div>
        <div>3 →</div>
    </div>

.. raw:: html

    <div class="flex w-50 pa2 ba b--red">
        <div class="ba pa4 tc"><span class="f1">1 →</span></div>
        <div class="ba pa4 tc"><span class="f1">2 →</span></div>
        <div class="ba pa4 tc"><span class="f1">3 →</span></div>
    </div>

Example of a reverse row container:

.. code:: html

    <div class="flex reverse row">
        <div>← 1</div>
        <div>← 2</div>
        <div>← 3</div>
    </div>

.. raw:: html

    <div class="flex reverse row w-50 pa2 ba b--red">
        <div class="ba pa4 tc"><span class="f1">← 1</span></div>
        <div class="ba pa4 tc"><span class="f1">← 2</span></div>
        <div class="ba pa4 tc"><span class="f1">← 3</span></div>
    </div>

It is worth noting that the ``row`` class is completely optional and is
specified only to ease the understanding in plain english.

The next example shows how the ``grow`` class impact a child item:

.. code:: html

    <div class="flex">
        <div>1 →</div>
        <div class="grow">2 →</div>
        <div>3 →</div>
    </div>

.. raw:: html

    <div class="flex w-50 pa2 ba b--red">
        <div class="ba pa4 tc"><span class="f1">1 →</span></div>
        <div class="grow ba pa4 tc"><span class="f1">2 →</span></div>
        <div class="ba pa4 tc"><span class="f1">3 →</span></div>
    </div>

The following examples show the differences between the two distribution
strategies along the main axis:

.. code:: html

    <div class="evenly-spaced flex row">...</div>

.. raw:: html

    <div class="evenly-spaced flex w-50 pa2 ba b--red">
        <div class="ba pa4 tc"><span class="f1">1 →</span></div>
        <div class="ba pa4 tc"><span class="f1">2 →</span></div>
        <div class="ba pa4 tc"><span class="f1">3 →</span></div>
    </div>

.. code:: html

    <div class="evenly-filled flex row">...</div>

.. raw:: html

    <div class="evenly-filled flex w-50 pa2 ba b--red">
        <div class="ba pa4 tc"><span class="f1">1 →</span></div>
        <div class="ba pa4 tc"><span class="f1">2 →</span></div>
        <div class="ba pa4 tc"><span class="f1">3 →</span></div>
    </div>

Finally the same goes for the vertical direction with the use of the ``column``
class:

.. raw:: html

    <div class="evenly-filled flex w-50">
        <div class="flex column h5 pa2 ba b--red">
            <div class="ba pa4 tc"><span class="f1">1 ↓</span></div>
            <div class="ba pa4 tc"><span class="f1">2 ↓</span></div>
            <div class="ba pa4 tc"><span class="f1">3 ↓</span></div>
        </div>
        <div class="flex reverse column h5 pa2 ba b--red">
            <div class="ba pa4 tc"><span class="f1">1 ↑</span></div>
            <div class="ba pa4 tc"><span class="f1">2 ↑</span></div>
            <div class="ba pa4 tc"><span class="f1">3 ↑</span></div>
        </div>
        <div class="evenly-spaced flex column h5 pa2 ba b--red">
            <div class="ba pa4 tc"><span class="f1">1 ↓</span></div>
            <div class="ba pa4 tc"><span class="f1">2 ↓</span></div>
            <div class="ba pa4 tc"><span class="f1">3 ↓</span></div>
        </div>
        <div class="evenly-filled flex column h5 pa2 ba b--red">
            <div class="ba pa4 tc"><span class="f1">1 ↓</span></div>
            <div class="ba pa4 tc"><span class="f1">2 ↓</span></div>
            <div class="ba pa4 tc"><span class="f1">3 ↓</span></div>
        </div>
    </div>

Advanced usages are available in the component gallery.


Source code
===========

.. include:: ../../air/src/layout/flex.css
    :code: css
    :start-after: */
