// Imports
import React from "react";
import { Component } from "react";
// React-Strap Elements
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label
} from "reactstrap";


/*
We skip the class definition and pass it to the export directly.

Custom Modal will receive 3 props:
    activeItem: The To-do item to be edited,
    toggle: Function used to control the Modal's state (open or close),
    onSave: Is called to save the edited values of the To-do item.

* */
export default class CustomModal extends Component{
    constructor(props) {
        super(props);
        this.state = {
            activeItem: this.props.activeItem,
        };
    }


    handleChange = (e) => {
        let { name, value } = e.target;

        if(e.target.type === "checkbox"){
            value = e.target.checked;
        }

        const activeItem = { ...this.state.activeItem, [name]: value };

        this.setState({ activeItem });

    };

    render() {
        const { toggle, onSave } = this.props;

        return(
            <Modal isOpen={ true } toggle={toggle}>
                <ModalHeader toggle={ toggle }>To-do Item</ModalHeader>
                <ModalBody>
                    {/*
                        Here we will define the three fields of the form: Title, Descripcion, Completed.
                    */}
                    <Form>
                        <FormGroup>
                            <Label for="todo-title">Title</Label>
                            <Input
                                type="text"
                                id="todo-title"
                                name="title"
                                value={ this.state.activeItem.title }
                                onChange={ this.handleChange }
                                placeholder="Enter Todo Title"
                                />
                        </FormGroup>
                        <FormGroup>
                            <Label for="todo-description">Descrition</Label>
                            <Input
                                type="text"
                                id="todo-description"
                                name="description"
                                value={ this.state.activeItem.description }
                                onChange={ this.handleChange }
                                placeholder="Enter Description"
                                />
                        </FormGroup>
                        <FormGroup check>
                            <Label check>
                                <Input
                                    type="checkbox"
                                    name="completed"
                                    checked={ this.state.activeItem.completed }
                                    onChange={ this.handleChange }
                                    />
                                Completed
                            </Label>
                        </FormGroup>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button
                        color="success"
                        onClick={() => onSave(this.state.activeItem)}
                        >
                        Save
                    </Button>
                </ModalFooter>
            </Modal>
        );
    }
}


