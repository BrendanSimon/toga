import toga

from toga.style import Pack

from toga.style.pack import (
    COLUMN,
    ROW,
    CENTER,
    LEFT,
    RIGHT,
)



PADDING = 5



class TogaDemo(toga.App):

    def startup(self):
        """
        Main entry point for app.
        """

        # Create the main window
        self.main_window = toga.MainWindow(self.name)

        # create optioncontainer
        self.option_container = toga.OptionContainer(on_select=self.option_container_handler)

        # Add a number of options that contain buttons
        self.add_option_buttons()

        # uncomment this line to add more options to demonstrate the "more navigator" (iOS)
        #self.add_option_more()

        self.main_window.content = self.option_container

        # Show the main window
        self.main_window.show()

    def add_option_buttons(self):
        """
        Add a set of buttons as an option to OptionController.
        """

        #! use same labels as iOS Clock app as an example
        for opt_label in [ 'World Clock', 'Alarm', 'Bedtime', 'Stopwatch', 'Timer' ] :            
            box = toga.Box( id=opt_label, style=Pack( direction=COLUMN, alignment=CENTER ) )

            # spacer
            box.add( toga.Box( style=Pack( flex=1 ) ) )

            for num in range( 1, 10 ) :
                but_label = f'{opt_label}: {num}'
                box.add(
                    toga.Button(
                        but_label,
                        on_press=self.button_handler,
                        style=Pack( padding=PADDING, alignment=CENTER ),
                    )
                )

            # spacer
            box.add( toga.Box( style=Pack( flex=1 ) ) )

            self.option_container.add( opt_label, box )

    def add_option_more(self):
        """
        Add some more options to demonstrate the "more navigation controller" (iOS).
        """

        for opt_label in [ 'Apple', 'Banana', 'Cherry', 'Dewberry' ] :
            box = toga.Box( id=opt_label, style=Pack( direction=COLUMN, alignment=CENTER ) )

            # spacer
            box.add( toga.Box( style=Pack( flex=1 ) ) )

            for num in range( 1, 10 ) :
                sw_label = f'{opt_label}: {num}'
                box.add(
                    toga.Switch(
                        sw_label,
                        on_toggle = self.switch_handler,
                        style = Pack( padding=PADDING, alignment=CENTER ),
                    )
                )

            # spacer
            box.add( toga.Box( style=Pack( flex=1 ) ) )

            self.option_container.add( opt_label, box )

    # def on_select_handler(self, widget):
    # def on_select_handler(self, interface, option):
    #     print( f'option container on select: interface={interface!r}, option={option!r}, option.id={option.id!r}' )
    def option_container_handler(self, option_container, option=None, index=None):
        print( f'option container on select: option_container={option_container!r}, option={option!r}, option.id={option.id!r}, index={index!r}' )

    def button_handler(self, button):
        print( f'button press: {button.label!r}')

    def switch_handler(self, switch):
        state = ( 'off', 'on' )[ switch.is_on ]
        print( f'switch {switch.label!r} state is now {state!r}' )



def main():
    return TogaDemo('Toga Demo', 'org.beeware.toga-demo')
