Display
#######

:icon: artboard-2-line.svg
:summary: The display property sets an element's inner and outer display types.
    The outer type sets an element's participation in flow layout; the inner
    type sets the layout of children.


Formally, the display property sets an element's inner and outer display types. The
outer type sets an element's participation in flow layout; the inner type sets the
layout of children. Some values of display are fully defined in their own individual
specifications; for example the detail of what happens when display: flex is declared is
defined in the CSS Flexible Box Model specification.


Mnemonics
=========

.. mnemonics:: air/src/layout/display.css


Note
====

Is is possible to use the class ``.flex`` instead of ``.df`` for back-compatibility
purpose and better self-explanatory layouts. Despite being defined in the *display*
module of Air, detailed explanation of its usage are available in its dedicated section
of the documentation.

Read also: aircss/typography/flexbox


Examples
========

If not specified, block will inherently set width to 100% of its parent element. It will
also cause a line break, even if the declared width doesn't take up the full width of
the parent.

.. code:: html

    <span class="db">
        display: block;
    </span>
    <span class="db w4">
        display: block;
    </span>

.. raw:: html

    <div class="mb6">
        <span class="db w4 ba b--ecume-80  bg--ecume-60 pa2 f7 source">
            display: block;
        </span>
        <span class="db ba b--ecume-80  bg--ecume-60 pa2 f7 source">
            display: block;
        </span>
    </div>


Set content inline. Inline doesn't respect height or width values. It does not render
white space between elements.

.. code:: html

    <span class="di">
        display: inline;
    </span>
    <span class="di">
        display: inline;
    </span>

.. raw:: html

    <div class="mb6">
        <span class="di ba b--ecume-80  bg--ecume-60 pa2 f7 source">
          display: inline;
        </span>
        <span class="di ba b--ecume-80  bg--ecume-60 pa2 f7 source">
          display: inline;
        </span>
    </div>


Inline-block will wrap around content inline. It also allows you to set height and width
properties on the element, which display inline does not allow you to do. It does render
the white-space in-between elements, so if you set width: 25% to four elements they will
not just render as a 4 column layout by default. For this latter use case, a flexbox
based solution should be a better way to achieve it.

.. code:: html

    <span class="dib">
        display: inline-block;
    </span>
    <span class="dib">
        display: inline-block;
    </span>


.. raw:: html

    <div class="mb6">
        <span class="dib ba b--ecume-80  bg--ecume-60 pa2">
          display: inline-block;
        </span>
        <span class="dib ba b--ecume-80  bg--ecume-60 pa2">
          display: inline-block;
        </span>
    </div>


You can set the display of any element to none by tacking on the ``.dn`` class.

.. code:: html

    <span class="dn ba b--ecume-80  bg--ecume-60 pa2">
        display: none;
    </span>

.. raw:: html

      <div class="mb6">
        <span class="dn ba b--ecume-80  bg--ecume-60 pa2">
          display: none;
        </span>
      </div>


    </div>


Source code
===========

.. include:: ../../air/src/layout/display.css
    :code: css
    :start-after: */
