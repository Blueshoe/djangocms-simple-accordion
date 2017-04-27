==========================
django CMS Accordion
==========================  

A plugin for django CMS which provides you an easy way to add accordion tabs to your pages. It's minimalistic and can be easily customized via CSS.

.. image:: https://travis-ci.org/Blueshoe/djangocms-simple-accordion.svg?branch=master
    :target: https://travis-ci.org/Blueshoe/djangocms-simple-accordion
    :alt: Code analysis status

.. image:: https://cloud.githubusercontent.com/assets/3121306/25285817/d5607b10-26bb-11e7-9cd5-77914c52e885.png

.. image:: https://cloud.githubusercontent.com/assets/3121306/25285816/d55b2f66-26bb-11e7-8ee4-aa68508a9dc7.png


Installation
============

To get started using ``djangocms-simple-accordion``:

- install it with ``pip``::

    $ pip install djangocms-simple-accordion


- add the plugins to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'djangocms_accordion',
        ...
    )


- run ``migrate djangocms_accordion``.


Dependencies
=============
- Currently this plugin depends on bootstrap and glyphicons.


Customization
=============
You can just override some of the CSS rules. In order to find the correct one, nspect the generated HTML in the development tools in the browser of your choice.

However, here are some commonly used customization options to get you started:

**Tab-Icons**

.. code-block:: css

    .accordion-title .accordion-toggleIcon:after {
      font-size: 13px;
      content: '\e080';
    }
    .accordion-title.active .accordion-toggleIcon:after {
      content: '\e114';
    }

**Accordion Color**

.. code-block:: css

    .accordion {
      background-color: red;
    }

**Title font size**

.. code-block:: css

    .accordion-title {
      font-size: 20px;
    }

**Transition Time**

.. code-block:: css

    .u-accordion-transition {
      -webkit-transition: ease-in-out .2s;
      -moz-transition: ease-in-out .2s;
      -ms-transition: ease-in-out .2s;
      -o-transition: ease-in-out .2s;
      transition: ease-in-out .2s;
    }

If you feel like you need to customize the plugin more than what is easily possible with CSS, go ahead and copy the directory *djangocms_accordion* into your django project.
