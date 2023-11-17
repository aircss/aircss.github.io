Font weight
###########


Varying the font-weight of different pieces of text can help create contrast between
pieces of information. It can help call attention to a piece of content, or help to make
a smaller font-size a bit more readable.

.. raw:: html

    <table class="table-fixed collapse w-100">
        <tbody>
            <tr>
                <td class="ph4 br b--noir-30 tc f1 fw1 v-base">A</td>
                <td class="ph4 br b--noir-30 tc f1 fw2 v-base">A</td>
                <td class="ph4 br b--noir-30 tc f1 fw3 v-base">A</td>
                <td class="ph4 br b--noir-30 tc f1 fw4 v-base">A</td>
                <td class="ph4 br b--noir-30 tc f1 fw5 v-base">A</td>
                <td class="ph4 br b--noir-30 tc f1 fw6 v-base">A</td>
                <td class="ph4 br b--noir-30 tc f1 fw7 v-base">A</td>
                <td class="ph4 br b--noir-30 tc f1 fw8 v-base">A</td>
                <td class="ph4 b--noir-30 tc f1 fw9 v-base">A</td>
            </tr>
            <tr>
                <td class="pr3 pt2 tc f8 noir-50 bt br b--noir-30">.fw1</td>
                <td class="pr3 pt2 tc f8 noir-50 bt br b--noir-30">.fw2</td>
                <td class="pr3 pt2 tc f8 noir-50 bt br b--noir-30">.fw3</td>
                <td class="pr3 pt2 tc f8 noir-50 bt br b--noir-30">.fw4</td>
                <td class="pr3 pt2 tc f8 noir-50 bt br b--noir-30">.fw5</td>
                <td class="pr3 pt2 tc f8 noir-50 bt br b--noir-30">.fw6</td>
                <td class="pr3 pt2 tc f8 noir-50 bt br b--noir-30">.fw7</td>
                <td class="pr3 pt2 tc f8 noir-50 bt br b--noir-30">.fw8</td>
                <td class="pr3 pt2 tc f8 noir-50 bt b--noir-30">.fw9</td>
            </tr>
        </tbody>
    </table>

Mnemonics
=========

.. mnemonics:: air/src/typography/font-weight.css


Shorthand
=========

It is possible to use the class name ``.b`` instead of ``.fw-bold``.


Examples
========

.. code:: html

  <p class="fw1">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fw1 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="fw2">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fw2 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="fw3">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fw3 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="fw-normal">The quick brown fox ...</p>
  <p class="fw4">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fw4 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="fw5">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fw5 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="fw6">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fw6 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="fw-bold">The quick brown fox ...</p>
  <p class="fw7">The quick brown fox ...</p>
  <p class="b">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fw7 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="fw8">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fw8 lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


Source code
===========

.. include:: ../../air/src/typography/font-weight.css
    :code: css
    :start-after: */
