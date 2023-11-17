Text transform
##############


Uppercase, title case and sentence can all be used in the same application. But if you
are using title case for headings, all headings need to be in title case. Likewise, you
can use sentence case for paragraphs. Use uppercase for standout texts only. The most
important thing is consistency.


Mnemonics
=========

.. mnemonics:: air/src/typography/text-transform.css


Examples
========

.. code:: html

  <p class="tts">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 tts lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="ttt">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 ttt lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="ttu">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 ttu lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


Source code
===========

.. include:: ../../air/src/typography/text-transform.css
    :code: css
    :start-after: */
