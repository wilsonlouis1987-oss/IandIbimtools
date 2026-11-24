# I&I BIM Tools

Dynamo graphs (.dyn) for Revit 2026 and Dynamo 3.x, covering project setup, modelling, interiors, drawings and issue. Built for ISO 19650 workflows.

## What is in this repo

- **59 Dynamo graphs** grouped by the letter at the start of the file name:

  - **A - Setup**: 11 graphs
  - **B - Model**: 25 graphs
  - **C - Interior**: 5 graphs
  - **D - Drawings**: 14 graphs
  - **E - Issue**: 4 graphs
- **RANDOM_RUBBLE_STONE.pat**: Revit fill pattern used by D07 (compound wall details).
- **streamlit_app.py**: a catalogue page that lists every graph with its description and a download button.

## How to use a graph

1. Download the `.dyn` file.
2. In Revit open **Manage > Dynamo**, then **Open** and pick the file.
3. Read the graph description, set the inputs (many use an Excel list or a linked CAD file) and press **Run**.

The graphs run only inside Revit. The Streamlit page is a library, not an online runner.

## Run the catalogue on your own machine

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy online

1. Upload these files to your GitHub repo.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Create an app, choose this repo, branch `main`, main file `streamlit_app.py`.

## File naming

`<Letter><Number>_<CATEGORY>_<Description>.dyn`, for example `D05_DRAWINGS_Tile_Layout_Plan_Annotation_Sheet.dyn`.

## Index

### A - Setup

- `A00_SETUP_New_Project_ISO19650_Worksets_Templates_Views_Sheets.dyn`
- `A01_SETUP_Project_Info_Units_Shared_Parameters_From_Excel.dyn`
- `A02_SETUP_Levels_Create_Rename_Elevations_From_Excel.dyn`
- `A03_SETUP_Floor_Ceiling_Area_Plans_Per_Level_From_Excel.dyn`
- `A04_SETUP_Door_Window_Room_Finish_Sheet_Schedules_From_Excel.dyn`
- `A05_SETUP_ISO19650_Type_Names_Worksets_View_Templates.dyn`
- `A07_SETUP_Project_And_Dimension_Units_MM_CM_M_Feet_Inches.dyn`
- `A08_SETUP_Revit_Colours_Ribbon_Properties_Project_Browser_Background.dyn`
- `A09_SETUP_Client_BIM_Requirements_BEP_AIR_COBie_FM_MIDP_Materials_Import_Setup_Check.dyn`
- `A10_SETUP_View_Discipline_SubDiscipline_Lighting_HVAC_Plumbing_Fire.dyn`
- `A11_SETUP_View_Templates_Per_Discipline_Sub_Discipline.dyn`

### B - Model

- `B01_MODEL_Grids_From_CAD_Grid_Lines_And_Bubbles.dyn`
- `B02_MODEL_Grids_On_Wall_Centrelines.dyn`
- `B03_MODEL_Walls_From_CAD_Double_Lines.dyn`
- `B04_MODEL_Doors_From_CAD_Swing_Arcs.dyn`
- `B05_MODEL_Selected_Columns_Resize_Rotate_Height.dyn`
- `B06_MODEL_Footings_Plinth_Beams_Top_Beams_From_Columns.dyn`
- `B07_MODEL_Slabs_On_Columns_Walls_Between_Columns_Copy_To_Levels.dyn`
- `B08_MODEL_Roof_From_Revit_Lines_Or_CAD_Roof_Plan.dyn`
- `B09_MODEL_Concrete_Stairs_From_CAD_Stair_Layers.dyn`
- `B10_MODEL_Concrete_Stairs_Inside_Stair_Rooms.dyn`
- `B11_MODEL_Wall_Slab_Openings_For_Pipes_Ducts_Trays.dyn`
- `B12_MODEL_Line_To_Wall_CAD_To_Wall_With_Doors.dyn`
- `B13_MODEL_Wall_Type_Layers_From_Section_Detail_Image.dyn`
- `B14_MODEL_3D_Walls_Doors_Windows_From_Plan_Image_Or_PDF.dyn`
- `B15_MODEL_Shaft_Openings_From_X_Lines_Revit_Or_CAD.dyn`
- `B16_MODEL_Slab_On_Outer_Wall_Perimeter_Or_CAD_Copy_To_Levels.dyn`
- `B17_MODEL_Floor_Tile_Pattern_From_Image.dyn`
- `B18_MODEL_Stairs_From_Revit_Lines_Or_CAD_Tread_Lines.dyn`
- `B19_MODEL_Structural_Columns_Beams_From_Plan_Grids_Or_Walls.dyn`
- `B20_MODEL_Doors_Windows_Clear_Of_Columns_Shift_Along_Wall.dyn`
- `B21_MODEL_Lintels_Headers_Jamb_Posts_For_Doors_Windows.dyn`
- `B22_MODEL_Grids_From_Image_Or_CAD_With_Bubbles_Names.dyn`
- `B23_MODEL_Copy_Elements_To_Levels_Above_Walls_Columns_Stairs_Floors_Doors_Windows_Facade.dyn`
- `B24_MODEL_Automatic_Stair_Generator_Straight_L_U_Dogleg_Multiflight_Landings_All_Levels.dyn`
- `B25_MODEL_AI_Structural_Genius_Columns_Beams_Footings_From_Architectural_Model.dyn`

### C - Interior

- `C01_INTERIOR_Room_Names_Finishes_Target_Area_From_Excel.dyn`
- `C02_INTERIOR_False_Ceilings_Bulkheads_Per_Room_From_CAD.dyn`
- `C03_INTERIOR_Wall_Skirting_Inside_Outside_Faces.dyn`
- `C04_INTERIOR_Door_Window_Marks_By_Room_And_Tags_From_Excel.dyn`
- `C05_INTERIOR_Spot_Lights_Between_Centre_Grid_Rows_Lighting_RCP.dyn`

### D - Drawings

- `D01_DRAWINGS_ISO19650_Sheets_And_Views_From_Excel_Drawing_List.dyn`
- `D02_DRAWINGS_Place_Each_View_On_Own_Sheet.dyn`
- `D03_DRAWINGS_Grid_Dimensions_And_Size_Tags_On_Sheet_Views.dyn`
- `D04_DRAWINGS_RCP_Sheet_Ceiling_Colour_Plan_Legend_Schedule.dyn`
- `D05_DRAWINGS_Tile_Layout_Plan_Annotation_Sheet.dyn`
- `D06_DRAWINGS_Revisions_P01_P02_On_Sheets_From_Excel.dyn`
- `D07_DRAWINGS_Compound_Wall_Footing_PCC_Rubble_Cladding_Dims_Labels.dyn`
- `D08_DRAWINGS_Match_Sheet_View_Crop_Scale_Position_To_Reference_Sheet.dyn`
- `D09_DRAWINGS_Sheets_From_View_List_Names_Numbers_Scales_Legends_Schedules.dyn`
- `D11_DRAWINGS_Auto_Annotate_Rooms_Doors_Windows_Walls_Tags_Grid_Dimensions.dyn`
- `D12_DRAWINGS_Tiling_Plan_Room_Tags_Tile_Start_Module_Dims_FFL_Levels_On_Sheet.dyn`
- `D13_DRAWINGS_Area_Statement_FAR_Coverage_Area_Plans_Sheet_Excel.dyn`
- `D14_DRAWINGS_Typical_Details_Wall_Window_Floor_Roof_Stair_Toilet_Sections_Annotated_Sheets.dyn`
- `D15_DRAWINGS_Elevation_Section_Sheet_Template_Colour_Depth_Levels_Grids_Dims_Spots_Tags_Fit_Scale.dyn`

### E - Issue

- `E01_ISSUE_Model_QA_Report_To_Excel_Before_Issue.dyn`
- `E02_ISSUE_Export_PDF_DWG_ISO_Names_Transmittal_Register.dyn`
- `E03_ISSUE_Export_PDF_DWG_IFC_NWC_Current_Or_Batch_Sheets.dyn`
- `E03_ISSUE_Export_PDF_DWG_IFC_NWC_Settings_In_Script.dyn`

## Licence

Apache License 2.0. See [LICENSE](LICENSE).
