//
//  CustomCameraView.swift
//  hackathonProject23
//
//  Created by Harry on 4/15/23.
//

import SwiftUI

struct CustomCameraView: View {
    
    let cameraService = CameraService()
    @Binding var capturedImage: UIImage?
    
    //@Environment(\.presentationMode) private var presentationMode
    
    var body: some View {
        ZStack{
            CameraView(cameraService: cameraService) { result in
                switch result {
                case .success(let photo):
                    if let data = photo.fileDataRepresentation() {
                        capturedImage = UIImage(data: data)
                        
                        let directoryURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
                        
                        let fileURL = URL(filePath: "image", relativeTo: directoryURL).appendingPathExtension("jpeg")
                        
                        do {
                            
                            try data.write(to: fileURL)
                            print("File Saved: \(fileURL.absoluteURL)")
                            
                        } catch {
                            
                            print(error.localizedDescription)
                            
                        }
                        
                        
                        //presentationMode.wrappedValue.dismiss()
                    } else {
                        
                        print("Error: no image data found:")
                        
                    }
                case .failure(let err):
                            print(err.localizedDescription)
                }
            }
            
            VStack{
                Spacer()
                Button(action: {
                    
                    cameraService.capturePhoto()
                    
                }, label: {
                    Image(systemName: "circle")
                        .font(.system(size: 72))
                        .foregroundColor(.white)

                })
                
            }
            
        }
    }
}
