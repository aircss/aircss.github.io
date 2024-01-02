Text decoration
###############

:icon: underline.svg
:summary: Underline and strikethrough decorations on a text are respectively
    used to add an emphasis or epanorthosis to all or part of it.


Underline and strikethrough decorations on a text are respectively used to add an
emphasis or epanorthosis to all or part of it.


Mnemonics
=========

.. mnemonics:: air/src/typography/text-decoration.css


Shorthand
=========

It is possible to use the class name ``.u`` instead of ``.td-underline``.


Examples
========

.. code:: html

  <p class="td-normal">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 td-normal lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>

.. code:: html

  <p class="td-strike">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 td-strike lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>

.. code:: html

  <p class="td-underline">The quick brown fox ...</p>
  <p class="u">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 u lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>

Source code
===========

.. include:: ../../air/src/typography/text-decoration.css
    :code: css
    :start-after: */
