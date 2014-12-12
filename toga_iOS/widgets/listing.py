from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from rubicon.objc import objc_method

from ..libs import (
    NSObject, UITableView, UITableViewCell,
    UITableViewCellStyleDefault,
)
from .base import Widget


class ListingImplHelper(NSObject):

    # Data source.

    @objc_method('@@@')
    def tableView_cellForRowAtIndexPath_(self, table, index_path):
        cell = table.dequeueReusableCellWithIdentifier_(None)
        if cell is None:
            cell = UITableViewCell.alloc().initWithStyle_reuseIdentifier_(
                UITableViewCellStyleDefault, None,
            )
        data = self.__dict__['interface']._data
        section, row = index_path.section, index_path.row

        list_item = data[section]['children'][row]
        if list_item.title:
            cell.textLabel.setText_(list_item.title)
        if list_item.subtitle:
            cell.detailTextLabel.setText_(list_item.subtitle)
        return cell

    @objc_method('i@')
    def numberOfSectionsInTableView_(self, table):
        return len(self.__dict__['interface']._data)

    @objc_method('i@i')
    def tableView_numberOfRowsInSection_(self, table, section):
        return len(self.__dict__['interface']._data[section]['children'])

    @objc_method('@@i')
    def tableView_titleForHeaderInSection_(self, table, section):
        return self.__dict__['interface']._data[section]['header']

    @objc_method('@@i')
    def tableView_titleForFooterInSection_(self, table, section):
        return self.__dict__['interface']._data[section]['footer']

    # Delegate.

    @objc_method('v@@')
    def tableView_didSelectRowAtIndexPath_(self, table, index_path):
        section, row = index_path.section, index_path.row
        interface = self.__dict__['interface']
        list_item = interface._data[section]['children'][row]
        if list_item.on_click:
            list_item.on_click(list_item)


class Listing(Widget):

    def __init__(self):
        super(Listing, self).__init__()
        self._data = []
        self.startup()

    def startup(self):
        self._impl = UITableView.alloc().init()
        helper = ListingImplHelper.alloc().init()
        helper.__dict__['interface'] = self
        self._impl.setDataSource_(helper)
        self._impl.setDelegate_(helper)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    def insert_section(self, index=None, header=None, footer=None):
        if index is None:
            index = len(self._data)
        elif index < 0:
            index = len(self._data) + index + 1
        self._data.insert(index, {
            'header': header,
            'footer': footer,
            'children': [],
        })
        return index

    def insert_row(self, section, index, item):
        children = self._data[section]['children']
        if index is None:
            index = len(children)
        elif index < 0:
            index = len(children) + index + 1
        children.insert(index, item)
        return index


class ListItem(object):

    def __init__(self, title, subtitle=None, on_click=None):
        super(ListItem, self).__init__()
        self.title = title
        self.subtitle = subtitle
        self.on_click = on_click
