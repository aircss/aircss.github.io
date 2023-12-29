Coordinates
###########

The coordinates sets where an element is positioned inside of a document or another
element.


Mnemonics
=========

.. mnemonics:: air/src/layout/coordinates.css


Examples
========

This example shows how absolute elements are absolutely positioned inside of a relative
element with a lot of padding (``.pa7``). The absolute element outer margin snapping to
the containing element is highlighted in each case.

.. raw:: html

    <div class="relative w-100 w-50-m h4 ba pa7 mb4">
        <div class="absolute top bl b--noir-30 h-100"></div>
        <div class="absolute left bt b--noir-30 w-100"></div>

        <div class="absolute top bt bw2 b--ecume-80 bg--ecume-60 pa3 tc f7">.top</div>
        <div class="absolute right br bw2 b--ecume-80 bg--ecume-60 pa3 tc f7">.right</div>
        <div class="absolute bottom bb bw2 b--ecume-80 bg--ecume-60 pa3 tc f7">.bottom</div>
        <div class="absolute left bl bw2 b--ecume-80 bg--ecume-60 pa3 tc f7">.left</div>

        <div class="absolute top left bt bl bw2 b--ecume-80 bg--ecume-60 pa3 tc f7">.top .left</div>
        <div class="absolute top right bt br bw2 b--ecume-80 bg--ecume-60 pa3 tc f7">.top .right</div>
        <div class="absolute bottom right bb br bw2 b--ecume-80 bg--ecume-60 pa3 tc f7">.bottom .right</div>
        <div class="absolute bottom left bb bl bw2 b--ecume-80 bg--ecume-60 pa3 tc f7">.bottom .left</div>

        <div class="absolute bg--ecume-60 pa3 f7 i">no coordinate</div>
    </div>


Source code
===========

.. include:: ../../air/src/layout/coordinates.css
    :code: css
    :start-after: */
