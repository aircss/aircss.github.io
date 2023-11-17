Tracking
########


Tracking affects the visual density of a word, phrase or paragraph. Decreasing the
tracking makes the words appear more compact, while increasing tracking increases the
amount of white space between letters and words, creating a more airy effect.


Mnemonics
=========

.. mnemonics:: air/src/typography/tracking.css


Shorthand
=========

It is possible to use the class name ``.tracked`` instead of ``.tracked-large``.


Examples
========

.. code:: html

  <p class="tracked-tight">The quick brown fox ...</p>

.. raw:: html

    <p class="f3 tracked-tight lh-body mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
    </p>

.. code:: html

  <p class="tracked-large">The quick brown fox ...</p>
  <p class="tracked">The quick brown fox ...</p>

.. raw:: html

    <p class="f3 tracked-large lh-body mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
    </p>

.. code:: html

  <p class="tracked-oversize">The quick brown fox ...</p>

.. raw:: html

    <p class="f3 tracked-oversize lh-body mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
    </p>


Source code
===========

.. include:: ../../air/src/typography/tracking.css
    :code: css
    :start-after: */
