Position
########

:icon: layout-top-2-line.svg
:summary: The position sets how an element is positioned in a document. This
    module should be used in conjunction with the coordinates module.


The position sets how an element is positioned in a document. This module should be used
in conjunction with the coordinates module.


Mnemonics
=========

.. mnemonics:: air/src/layout/position.css


Description
===========

``.fixed``

When fixed, the element is removed from the normal document flow, and no space is
created for the element in the page layout. The element is positioned relative to its
initial containing block, which is the viewport in the case of visual media.


``.aboslute``

Absolute elements are absolutely positioned inside of a relative element. You can use
absolute positioning to stretch elements making sure they fill the width and height of a
relative container.


``.relative``

Relatively positioned elements offer the ability to offset the position of an element
without affecting the position of any elements around it.


``.sticky``

Sticky elements are positioned normally in the document flow, and then offset relative
to its nearest scrolling ancestor and containing block.


Source code
===========

.. include:: ../../air/src/layout/position.css
    :code: css
    :start-after: */
