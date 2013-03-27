# -*- coding: utf-8 -*-
#
# Copyright © 2013 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the License
# (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied, including the
# implied warranties of MERCHANTABILITY, NON-INFRINGEMENT, or FITNESS FOR A
# PARTICULAR PURPOSE.
# You should have received a copy of GPLv2 along with this software; if not,
# see http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

COMMON_SPEC_URL = 'http://linux.duke.edu/metadata/common'

PACKAGE_TAG = 'newpackage'

def process_package_element(element):
    delta = element.find('delta')
    filename = delta.find('filename')
    sequence = delta.find('sequence')
    size = delta.find('size')
    checksum = delta.find('checksum')

    return {
        'type': 'drpm',
        'new_package': element.attrib['name'],
        'epoch': element.attrib['epoch'],
        'version': element.attrib['version'],
        'release': element.attrib['release'],
        'arch': element.attrib['arch'],
        'oldepoch': delta.attrib['oldepoch'],
        'oldversion': delta.attrib['oldversion'],
        'oldrelease': delta.attrib['oldrelease'],
        'filename': filename.text,
        'sequence': sequence.text,
        'size': int(size.text),
        'checksum': size.text,
        'checksumtype': checksum.attrib['type'],
    }