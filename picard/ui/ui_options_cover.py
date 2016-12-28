# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CoverOptionsPage(object):
    def setupUi(self, CoverOptionsPage):
        CoverOptionsPage.setObjectName(_fromUtf8("CoverOptionsPage"))
        CoverOptionsPage.resize(632, 560)
        self.verticalLayout = QtGui.QVBoxLayout(CoverOptionsPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.location = QtGui.QGroupBox(CoverOptionsPage)
        self.location.setObjectName(_fromUtf8("location"))
        self.vboxlayout = QtGui.QVBoxLayout(self.location)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(2)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.save_images_to_tags = QtGui.QCheckBox(self.location)
        self.save_images_to_tags.setObjectName(_fromUtf8("save_images_to_tags"))
        self.vboxlayout.addWidget(self.save_images_to_tags)
        self.cb_embed_front_only = QtGui.QCheckBox(self.location)
        self.cb_embed_front_only.setObjectName(_fromUtf8("cb_embed_front_only"))
        self.vboxlayout.addWidget(self.cb_embed_front_only)
        self.save_images_to_files = QtGui.QCheckBox(self.location)
        self.save_images_to_files.setObjectName(_fromUtf8("save_images_to_files"))
        self.vboxlayout.addWidget(self.save_images_to_files)
        self.label_use_filename = QtGui.QLabel(self.location)
        self.label_use_filename.setObjectName(_fromUtf8("label_use_filename"))
        self.vboxlayout.addWidget(self.label_use_filename)
        self.cover_image_filename = QtGui.QLineEdit(self.location)
        self.cover_image_filename.setObjectName(_fromUtf8("cover_image_filename"))
        self.vboxlayout.addWidget(self.cover_image_filename)
        self.save_images_overwrite = QtGui.QCheckBox(self.location)
        self.save_images_overwrite.setObjectName(_fromUtf8("save_images_overwrite"))
        self.vboxlayout.addWidget(self.save_images_overwrite)
        self.cb_autofit_coverart = QtGui.QCheckBox(self.location)
        self.cb_autofit_coverart.setObjectName(_fromUtf8("cb_autofit_coverart"))
        self.vboxlayout.addWidget(self.cb_autofit_coverart)
        self.coverart_resize_options = QtGui.QHBoxLayout()
        self.coverart_resize_options.setObjectName(_fromUtf8("coverart_resize_options"))
        self.label_resize_text = QtGui.QLabel(self.location)
        self.label_resize_text.setMouseTracking(False)
        self.label_resize_text.setToolTip(_fromUtf8(""))
        self.label_resize_text.setObjectName(_fromUtf8("label_resize_text"))
        self.coverart_resize_options.addWidget(self.label_resize_text)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.coverart_resize_options.addItem(spacerItem)
        self.label_resize_width = QtGui.QLabel(self.location)
        self.label_resize_width.setObjectName(_fromUtf8("label_resize_width"))
        self.coverart_resize_options.addWidget(self.label_resize_width)
        self.resize_width = QtGui.QSpinBox(self.location)
        self.resize_width.setEnabled(True)
        self.resize_width.setMinimum(1)
        self.resize_width.setMaximum(10000)
        self.resize_width.setSingleStep(1)
        self.resize_width.setProperty("value", 250)
        self.resize_width.setObjectName(_fromUtf8("resize_width"))
        self.coverart_resize_options.addWidget(self.resize_width)
        self.label_resize_height = QtGui.QLabel(self.location)
        self.label_resize_height.setObjectName(_fromUtf8("label_resize_height"))
        self.coverart_resize_options.addWidget(self.label_resize_height)
        self.resize_height = QtGui.QSpinBox(self.location)
        self.resize_height.setMinimum(1)
        self.resize_height.setMaximum(10000)
        self.resize_height.setProperty("value", 250)
        self.resize_height.setObjectName(_fromUtf8("resize_height"))
        self.coverart_resize_options.addWidget(self.resize_height)
        self.vboxlayout.addLayout(self.coverart_resize_options)
        self.verticalLayout.addWidget(self.location)
        self.ca_providers_groupbox = QtGui.QGroupBox(CoverOptionsPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ca_providers_groupbox.sizePolicy().hasHeightForWidth())
        self.ca_providers_groupbox.setSizePolicy(sizePolicy)
        self.ca_providers_groupbox.setObjectName(_fromUtf8("ca_providers_groupbox"))
        self.ca_providers_layout = QtGui.QVBoxLayout(self.ca_providers_groupbox)
        self.ca_providers_layout.setObjectName(_fromUtf8("ca_providers_layout"))
        self.ca_providers_list = QtGui.QHBoxLayout()
        self.ca_providers_list.setObjectName(_fromUtf8("ca_providers_list"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ca_providers_list.addItem(spacerItem1)
        self.ca_providers_layout.addLayout(self.ca_providers_list)
        self.verticalLayout.addWidget(self.ca_providers_groupbox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(CoverOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(CoverOptionsPage)
        CoverOptionsPage.setTabOrder(self.save_images_to_tags, self.cb_embed_front_only)
        CoverOptionsPage.setTabOrder(self.cb_embed_front_only, self.save_images_to_files)
        CoverOptionsPage.setTabOrder(self.save_images_to_files, self.cover_image_filename)
        CoverOptionsPage.setTabOrder(self.cover_image_filename, self.save_images_overwrite)

    def retranslateUi(self, CoverOptionsPage):
        self.location.setTitle(_("Location"))
        self.save_images_to_tags.setText(_("Embed cover images into tags"))
        self.cb_embed_front_only.setText(_("Only embed a front image"))
        self.save_images_to_files.setText(_("Save cover images as separate files"))
        self.label_use_filename.setText(_("Use the following file name for images:"))
        self.save_images_overwrite.setText(_("Overwrite the file if it already exists"))
        self.cb_autofit_coverart.setToolTip(_("Auto-fits (crops and resizes) images to the given dimensions"))
        self.cb_autofit_coverart.setText(_("Auto-fit coverart images"))
        self.label_resize_text.setText(_("Auto-fit coverart images to the following dimensions:"))
        self.label_resize_width.setText(_("W:"))
        self.label_resize_height.setText(_("H:"))
        self.ca_providers_groupbox.setTitle(_("Cover Art Providers"))

