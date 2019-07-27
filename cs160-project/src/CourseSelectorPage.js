import React from 'react'
import './App.css'



/**
 * Top level component for the second page of the application.
 * Contains
 *  A back button
 *  A array html buttons. 
 *  A next button
 *
 * props
 *  courses An array of class objects.
 *  handleToggle A function to be used for the onClick property of buttons
 *  backButton A onClick handler for the back button
 *  loadNextPage A onClick handler for the next button
 *
 */
class CourseSelectorPage extends React.Component {



  /**
   * Returns an array of class objects from the values stored in 
   * the lookupTable
   */
  getCoursesList() {
    let courses = []
    this.props.lookupTable.forEach( (value, key, map) => {
      courses.push({course: value, ID: key})
    } )
    return courses
  }



  /**
   * Maps the array of courses from props to an
   * array of toggle buttons. Button text is set to 
   * the course name, and the onClick is handled by the handleToggle prop
   */
  generateButtons() {
    let buttons = this.getCoursesList().map( (row) => {  
      let buttonName = row.course.isSelected ? 'selected' : 'not_selected'
      return(
        <button key={row.ID}
                className={'class_toggle_' + buttonName}
                onClick={ () => {this.props.handleToggle(row.ID)} }
        >
          {row.course.name}
        </button>
      )
    })
    return buttons
  }


  /**
   * Render function for the component. Places the back button,
   * the next button, and calls generateButtons() to render the 
   * toggle buttons for each class.
   */
  render() {
    return (
      <div className="page_two">

        <div align='right'>
        <button className="back_button"
                onClick={this.props.backButton}>Back</button>
        </div>
      
        <div className="class_selector">
          <h1> What classes have you completed at DUMMY DATA? </h1>
          <br/>

          <div className="class_selector_container">
            {this.generateButtons()}
          </div>
        
        </div>
        
         <div className="next_button_box">
            <button className="next_button"
                    onClick={this.props.loadNextPage}>Next</button>
          </div>

      </div>
    )
  }
}

export default CourseSelectorPage