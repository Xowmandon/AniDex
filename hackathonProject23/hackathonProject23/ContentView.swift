//
//  File.swift
//  hackathonProject23
//
//  Created by Harry on 4/15/23.
//

import SwiftUI

struct ContentView: View {
    
    @State private var capturedImage : UIImage? = nil
    @State private var isCustomCameraViewPresented = false
    
    var body: some View {
        
        CustomCameraView(capturedImage: $capturedImage)
        	
        /*
        ZStack {
            if capturedImage != nil {
                Image(uiImage: capturedImage!)
                    .resizable()
                    .scaledToFill()
                    .ignoresSafeArea()
            }
            VStack {
                Spacer()
                HStack {
                    Circle()
                        .frame(width: 50)
                        .clipped()
                        .overlay {
                            Image(systemName: "book.closed")
                                .symbolRenderingMode(.monochrome)
                                .foregroundColor(.black)
                                .font(.system(size: 30, weight: .regular, design: .default))
                                .frame(alignment: .center)
                                .clipped()
                        }
                    Button(action: {
                        
                        isCustomCameraViewPresented.toggle()
                        
                    }, label: {
                        
                        Circle()
                            .frame(width: 70)
                            .clipped()
                            .overlay {
                                Image(systemName: "camera.viewfinder")
                                    .symbolRenderingMode(.monochrome)
                                    .foregroundColor(.black)
                                    .font(.system(size: 40, weight: .regular, design: .default))
                                    .frame(alignment: .center)
                                    .clipped()
                            }
                        
                    })
                    .padding(.bottom)
                    .sheet(isPresented: $isCustomCameraViewPresented){
                        
                        CustomCameraView(capturedImage: $capturedImage)
                        
                    }
                    
                    Circle()
                        .frame(width: 50)
                        .clipped()
                        .overlay {
                            Image(systemName: "questionmark")
                                .symbolRenderingMode(.monochrome)
                                .foregroundColor(.black)
                                .font(.system(size: 30, weight: .regular, design: .default))
                                .frame(alignment: .center)
                                .clipped()
                        }
                }
                .padding(.bottom, 30)
            }
        }
        */
        /*
        ZStack {
            
            if capturedImage != nil {
                Image(uiImage: capturedImage!)
                    .resizable()
                    .scaledToFill()
                    .ignoresSafeArea()
            }
            
            VStack {
                Spacer()
                Button(action: {
                    
                    isCustomCameraViewPresented.toggle()
                    
                }, label: {
                    
                    Image (systemName: "camera.fill")
                        .font(.largeTitle)
                        .padding()
                        .background(Color.black)
                        .foregroundColor(.white)
                        .clipShape(Circle())
                    
                })
                .padding(.bottom)
                .sheet(isPresented: $isCustomCameraViewPresented){
                    
                    CustomCameraView(capturedImage: $capturedImage)
                    
                }
                
            }
            
        }
        */
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        
        ContentView()
        
    }
}
